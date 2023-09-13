# this program is used to converty directory into zips

import os
import pathlib
import sys
import zipfile

directoryName = input("Enter Directory name: ")

if not os.path.isdir(directoryName):
    print("Directory does not exits..")
    sys.exit(0)

currentDirectory = pathlib.Path(directoryName)

Zip = "Zip"

with zipfile.ZipFile(Zip, mode='w') as archive:
    for i in currentDirectory.rglob("*"):
        archive.write(i,arcname=i.relative_to(currentDirectory))

if os.path.isfile(Zip):
    print("zip created")
else:
    print("error!")
