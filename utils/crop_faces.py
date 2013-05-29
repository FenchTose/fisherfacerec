import os
from SimpleCV import *

imgs = []
#base = "Database"
#cropbase = "crop"
base = "emotions"
cropbase = "emotionscrop"
directory = os.listdir(base)
cascade = "/home/jay/SimpleCV/SimpleCV/Features/HaarCascades/face.xml"

for d in directory:
    files = os.listdir("/".join([base, d]))
    num=0
    try:
        os.mkdir("crop/"+d)
    except OSError:
        pass
    for f in files:
        print f
        if 'crop' in f:
            continue
        img = Image("/".join([base, d, f]))
        img.show()
        #img1 = img.resize(w=400, h=300)
        feat = img.findHaarFeatures(cascade)
        if feat:
            crop_image = feat.sortArea()[-1].crop()
            crop_image = crop_image.resize(w=200, h=200)
            crop_image.save("/".join([cropbase, d, "crop"+str(num)+".jpg"]))
            print "/".join([cropbase, d, "crop"+str(num)+".jpg"])
            #crop_image.save("crop/"+d+"/crop"+str(num)+".jpg")
            #print "crop/"+d+"/crop"+str(num)+".jpg"
        num+=1

