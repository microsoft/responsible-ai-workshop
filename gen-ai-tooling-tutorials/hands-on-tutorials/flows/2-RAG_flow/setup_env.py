import os
from typing import Union

from promptflow.core import tool
from promptflow.connections import AzureOpenAIConnection, OpenAIConnection

from utils.lock import acquire_lock

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "/chat_with_pdf/"


@tool
def setup_env(connection: Union[AzureOpenAIConnection, OpenAIConnection], config: dict):
    if not connection or not config:
        return

    if isinstance(connection, AzureOpenAIConnection):
        os.environ["OPENAI_API_TYPE"] = "azure"
        os.environ["OPENAI_API_BASE"] = connection.api_base
        os.environ["OPENAI_API_KEY"] = connection.api_key
        os.environ["OPENAI_API_VERSION"] = connection.api_version

    if isinstance(connection, OpenAIConnection):
        os.environ["OPENAI_API_KEY"] = connection.api_key
        if connection.organization is not None:
            os.environ["OPENAI_ORG_ID"] = connection.organization

    for key in config:
        os.environ[key] = str(config[key])
            
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    lock_path = os.path.join(BASE_DIR, "create_folder.lock")
    pdfs_dir = os.path.join(BASE_DIR, ".pdfs")
    index_pdfs_dir = os.path.join(BASE_DIR, ".index", ".pdfs")

    with acquire_lock(lock_path):
        if not os.path.exists(pdfs_dir):
            os.mkdir(pdfs_dir)
        if not os.path.exists(index_pdfs_dir):
            os.makedirs(index_pdfs_dir)        
    
    return "Ready"
