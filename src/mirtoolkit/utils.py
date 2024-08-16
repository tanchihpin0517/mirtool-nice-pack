import shutil
import subprocess
import tempfile
from pathlib import Path


def download(url, file):
    assert isinstance(url, str)
    assert isinstance(file, (str, Path))
    if isinstance(file, str):
        file = Path(file)

    if shutil.which("wget") is None:
        raise FileNotFoundError("wget not found. Please install wget.")
    # Download the file using wget
    tmp_dir = tempfile.TemporaryDirectory()
    tmp_file = tmp_dir.name + "/" + file.name
    subprocess.run(["wget", "-O", tmp_file, url], check=True)
    shutil.move(tmp_file, file)

    # try:
    #     # Send a GET request to the URL
    #     response = requests.get(url, stream=True)
    #     response.raise_for_status()  # Raise an error for bad status codes

    #     tmp_dir = tempfile.TemporaryDirectory()
    #     tmp_file = tmp_dir.name + "/" + file.name
    #     with open(tmp_file, "wb") as f:
    #         for chunk in response.iter_content(chunk_size=8192):
    #             f.write(chunk)
    #     shutil.move(tmp_file, file)
    # except requests.RequestException as e:
    #     print(f"An error occurred: {e}")
