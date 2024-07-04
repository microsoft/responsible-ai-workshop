from promptflow.core import tool
from download import download
import logging


@tool
def download_tool(urls: list, env_ready_signal: str) -> list:
    downloaded_files = []
    for url in urls:
        try:
            file_path = download(url)
            downloaded_files.append(file_path)
        except Exception as e:
            logging.error(f"Failed to download {url}: {e}")
    return downloaded_files