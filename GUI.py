import os
import tarfile
import time
import tkinter as tk
from zipfile import ZipFile

root = tk.Tk()
root.title("Build 3006G")
root.geometry("600x400")
path = tk.Entry(root, width=30)
path.pack(pady=20)
extractto = tk.Entry(root, width=30)
extractto.pack(pady=30)
label1 = tk.Label(root, text="Put your zip, jar, sb3, tar or tgz files in the first input.", font=("Arial", 8))
label2 = tk.Label(root, text="Then put the destination folder in the second and hit extract!", font=("Arial", 8))
label1.pack()
label2.pack()
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

def on_click():
  patha = path.get()
  extracttoa = extractto.get()
  if ".zip" in patha or ".jar" in patha or ".sb3" in patha:
        extract_single_zip(patha, extracttoa)
  elif ".tar" in path or ".tgz" in path:
        extract_tar_file(patha, extracttoa)

ExtractIt = tk.Button(root, text="Extract!", command=on_click)

ExtractIt.pack(pady=15)
root.mainloop()
