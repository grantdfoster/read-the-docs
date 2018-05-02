## How To: Search a Directory
*walking a directory and searching for a specific filetype*

### Uses
* os
* fnmatch
* tkinter

### Implementation
```python
# import necessary modules
import os
from fnmatch import fnmatch
from tkinter import filedialog

# set filetype filter and directory
filter_keyword = "*.pdf"
selected_directory = filedialog.askdirectory()

# walk directory and find files
file_paths = []
for path, subdirs, files in os.walk(selected_directory):
    for file_name in files:
        if fnmatch(file_name, filter_keyword):
            file_path = os.path.join(path, file_name)
            file_paths.append(os.path.abspath(file_path))

# open and read found files
for path in file_paths:
    with open(path, mode='rb') as fp:
        file = fp.read()

# print found file paths
print(file_paths)
```

[back](../README.md)
