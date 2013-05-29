import os
from SimpleCV import *
#base = "orl_faces"
#female = ["s8", "s10", "s32", "s35"]

base = "crop"
female = ["JLo", "Naomi", "Roberts", "Stone", "Emma", "Katy"]
database = "celebcrop"
mNo = 1
fNo = 1
dirs = os.listdir(base)
for d in dirs:
    files = os.listdir("/".join([base, d]))
    if d in female:
        for f in files:
            img = Image("/".join([base, d, f]))
            img.save("/".join([database, "female", str(fNo)])+".jpg")
            fNo+=1
    else:
        for f in files:
            img = Image("/".join([base, d, f]))
            img.save("/".join([database, "male", str(mNo)])+".jpg")
            mNo+=1

