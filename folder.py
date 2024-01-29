
from os import *
from os.path import *

cwd = getcwd()
name = input("Folder name : ")

path = join(cwd,name)

makedirs(path)

for outfolder in ("train","validate","test"):
    otFolder = join(path,outfolder)
    makedirs(otFolder)
    for infolder in ("images","labels"):
        makedirs(join(otFolder,infolder))