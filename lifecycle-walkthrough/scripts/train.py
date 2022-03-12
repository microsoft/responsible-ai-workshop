# Required Imports

import azureml.core
from azureml.core import Workspace
import shap # Data is collected through the shap library
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Connection to Azure ML workspace
ws = Workspace.from_config()
print(ws.name, ws.location, ws.resource_group, sep='\t')

# Data Loading
X_raw, Y = shap.datasets.adult()
df = pd.DataFrame(X_raw, Y)


# Data Preprocessing
categorical_features_indices = np.where(np.logical_or(X_raw.dtypes == np.int8, X_raw.dtypes == np.int32))[0]
numeric_features_indices = np.where(X_raw.dtypes == np.float32)[0]

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

column_transformer = ColumnTransformer ([
    ('onehot', OneHotEncoder(handle_unknown='ignore'),
    categorical_features_indices),
    ('scaler', StandardScaler(),
    numeric_features_indices)
])

# Data Labeling
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
print("Before label encoding:",Y)
Y=le.fit_transform(Y)
print("After label encoding:",Y) 

# Data Split and feature enrichment
A=X_raw[['Sex']]
X_train, X_test, Y_train, Y_test, A_train, A_test = train_test_split(
    X_raw, Y, A,
    test_size=0.2, random_state=0, stratify=Y)

X_train.reset_index(drop=True)
X_test.reset_index(drop=True)
A_train.reset_index(drop=True)
A_test.reset_index(drop=True)
pandas_warnings=pd.get_option('mode.chained_assignment')
pd.set_option('mode.chained_assignment', None)
# improve labels by replacing numbers with labels
A_test.Sex.loc[(A_test['Sex']==0)] = 'female'
A_test.Sex.loc[(A_test['Sex']==1)] = 'male'
pd.set_option('mode.chained_assignment', pandas_warnings)

X_train_new = column_transformer.fit_transform(X_train)
Y_train_new = Y_train

# Modeling
from catboost import CatBoostClassifier # !pip install catboost==0.18.1
model_1 = CatBoostClassifier(
    random_seed=42, logging_level="Silent", iterations=150)
model_catboost = model_1.fit(X_train_new, Y_train_new)
model_catboost.save_model(
    "catboost_predictor.onnx",
    format="onnx",
    export_parameters={
        'onnx_domain': 'ai.catboost',
        'onnx_model_version': 1,
        'onnx_doc_string': 'loan decision model',
        'onnx_graph_name': 'CatBoostModel_for_loan)decision'
    }
)

# Register model to Azure ML
from azureml.core.model import Model
model = Model.register(workspace=ws,
                       model_name='catboost_predictor_onnx',                  # Name of the registered model in your workspace.
                       model_path='catboost_predictor.onnx',              # Local ONNX model to upload and register as a model.
                       model_framework=Model.Framework.ONNX ,      # Framework used to create the model.
                       model_framework_version='1.3',              # Version of ONNX used to create the model.
                       description='Onnx loan decision model')