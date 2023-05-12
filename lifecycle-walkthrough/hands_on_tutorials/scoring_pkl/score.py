import joblib
import joblib
import os
import json
import pandas as pd

def init():
    # Create a global variable called model
    global model
    #Load the model from the path
    model = joblib.load(os.environ.get("MODEL_PATH")) 


def run(request):
   try:
     df = pd.read_json(request)
     result = model.predict(df)
     return {'data' : result.tolist() , 'message' : "Successfully classified loan"}
   except Exception as e:
      error = str(e)
      return {'data' : error , 'message' : "Failed to classify loan"}

