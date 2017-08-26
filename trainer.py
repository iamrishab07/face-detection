# import the libraries
import cv2
import os
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
path = 'dataSet'

def getImagesID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []
    # names = []
    for ImagePath in imagePaths:
        faceImage = Image.open(ImagePath).convert('L')
        faceNp = np.array(faceImage,'uint8')
        ID = int(os.path.split(ImagePath)[-1].split('.')[1])
        # name = os.path.split(ImagePath)[-1].split('.')[3]
        print ID
        # print name

        faces.append(faceNp)
        IDs.append(ID)
        # names.append(name)
        cv2.imshow("Windows",faceNp)
        cv2.waitKey(1000)
    return np.array(IDs), faces



Ids, faces = getImagesID(path)
recognizer.train(faces,Ids)

recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()
