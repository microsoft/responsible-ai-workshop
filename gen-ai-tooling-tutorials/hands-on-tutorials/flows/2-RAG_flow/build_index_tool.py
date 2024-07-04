from promptflow.core import tool
from build_index import create_faiss_index

@tool
def build_index_tool(pdf_paths: list) -> list:
    index_paths = [create_faiss_index(path) for path in pdf_paths]
    return index_paths