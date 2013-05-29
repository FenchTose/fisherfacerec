from SimpleCV import *

base = "emotionscrop"
moods = ["happyfaces", "sadfaces"]
moodlabels = ["happy", "sad"]

f = FaceRecognizer()
imgs = []
labels = []
for mood, label in zip(moods, moodlabels):
    print mood, label
    imgset = ImageSet("/".join([base, mood]))
    imgs +=imgset
    labels += [label]*len(imgset)
print len(imgs)
f.train(imgs, labels)

cam = Camera()

while True:
    try:
        img = cam.getImage()
        #img = Image("emotionscrop/happyfaces/crop0.jpg")
        retVal = img.findAndRecognizeFaces(f)
        if retVal is not None:
            print retVal
            feat, label, conf = retVal[0]
            img = feat.crop()
            img.drawText(label, fontsize=42)
        img.show()
        time.sleep(2)
    except KeyboardInterrupt:
        break
