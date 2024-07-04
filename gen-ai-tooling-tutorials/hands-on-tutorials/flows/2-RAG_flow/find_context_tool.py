from promptflow.core import tool
from find_context import find_context


@tool
def find_context_tool(question: str, index_paths: list[str]) -> dict:
    """    
    Returns:
    - dict: A dictionary containing the prompt and a list of contexts.
    """
    # Find the context for the given question using the provided index paths
    for index_path in index_paths:
        prompt, context = find_context(question, index_path)

    # Return the prompt and the context texts in a dictionary
    return {"prompt": prompt, "context": [c.text for c in context]}