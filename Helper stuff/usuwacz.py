import os
import random

path = os.path.join(os.path.dirname(__file__))

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
onlyfiles.remove("usuwacz.py")

print(onlyfiles)

for i in range(40):
    random_file = random.choice(onlyfiles)
    
    if os.path.exists(f"{path}/{random_file}"):
        os.remove(f"{path}/{random_file}")
    else:
        print("The file does not exist")
    onlyfiles.remove(random_file)