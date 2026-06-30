import os
import tarfile
from zipfile import ZipFile

def extract_single_zip(path, extractto):
    os.makedirs(extractto, exist_ok=True)
    with ZipFile(path, 'r') as archive:
        archive.extractall(path=extractto)
        print(f" Extracted '{path}' to '{extractto}' successfully")

def extract_tar_file(path, extractto):
    os.makedirs(extractto, exist_ok=True)
    with tarfile.open(path, 'r:*') as archive:
        archive.extractall(path=extractto)
        print(f" Extracted '{path}' to '{extractto}' successfully")

path = input("File path of Zip, TAR, JAR or Scratch project:")
extractto = input("Extract to: ")

if ".zip" in path or ".jar" in path or ".sb3" in path:
    extract_single_zip(path, extractto)
elif ".tar" in path or ".tgz" in path:
    extract_tar_file(path, extractto)
