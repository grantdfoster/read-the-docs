import os
from fnmatch import fnmatch
from tkinter import filedialog

filter_keyword = "*.pdf"
selected_directory = filedialog.askdirectory()

file_paths = []
for path, subdirs, files in os.walk(selected_directory):
    for file_name in files:
        if fnmatch(file_name, filter_keyword):
            file_path = os.path.join(path, file_name)
            file_paths.append(os.path.abspath(file_path))

print(file_paths)