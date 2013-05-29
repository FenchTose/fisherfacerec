import os
from SimpleCV import *

base = "celebcrop"
mimgs = ImageSet("/".join([base, "male"]))
fimgs = ImageSet("/".join([base, "female"]))
mlabels=[]
flabels=[]
f = FaceRecognizer()
#f.load("celebgenderdata.xml")
f.load("bitsgenderdata.xml")
#f.load("AT_T_Gender_Data.xml")
print "Male"
for img in mimgs:
    label = img.recognizeFace(f)
    if label is not None:
        mlabels.append(label)
print ""
print "Female"
for img in fimgs:
    label = img.recognizeFace(f)
    if label is not None:
        flabels.append(label)
print flabels
print float(sum(mlabels))/len(mlabels)*100, "% prediction for male."
print (1-float(sum(flabels))/len(flabels))*100, "% prediction for female."