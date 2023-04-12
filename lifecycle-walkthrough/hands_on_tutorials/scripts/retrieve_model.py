from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.authentication import ServicePrincipalAuthentication
import os

def main():
    workspace_name = os.environ.get("WORKSPACE_NAME")
    resource_group = os.environ.get("RESOURCE_GROUP_NAME")
    subscription_id = os.environ.get("SUBSCRIPTION_ID")
    tenant_id = os.environ.get("TENANT_ID")
    app_id = os.environ.get("SP_APP_ID")
    app_secret = os.environ.get("SP_APP_SECRET")
    model_name = os.environ.get('MODEL_NAME')

    svc_pr = ServicePrincipalAuthentication(tenant_id=tenant_id,service_principal_id=app_id,service_principal_password=app_secret)

    ws = Workspace.get(name=workspace_name,
               auth=svc_pr,
               subscription_id=subscription_id,
               resource_group=resource_group)

    model = Model(workspace=ws, name=model_name)
    file_name=model.download()
    os.rename(file_name,r'model.onnx')

if __name__ == '__main__':
    main()