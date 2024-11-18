import os
import shutil
import zipfile

directory = os.__file__
print(directory)
directory, filename = os.path.split(directory)
directory = directory+'\site-packages'
from_dir = "./mhi.zip"
to_dir = directory+"/mhi.zip"
shutil.move(from_dir, to_dir)

with zipfile.ZipFile(to_dir, 'r') as zip_ref:
    zip_ref.extractall(directory)
