import os
from SimpleCV import *

base = "bitscrop"

mimgs = ImageSet("/".join([base, "Male"]))
mlabels = [1]*len(mimgs)
fimgs = ImageSet("/".join([base, "Female"]))
flabels = [0]*len(fimgs)

imgs = mimgs + fimgs
labels = mlabels + flabels

f = FaceRecognizer()
f.train(imgs, labels)
f.save("bitsgenderdata.xml")