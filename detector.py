import cv2
import numpy as np
from PIL import Image
import pickle
import sqlite3

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer()
rec.load("recognizer\\trainingData.yml")
path = "dataSet"

def getProfile(id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Persons WHERE ID=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile



id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        profile = getProfile(id)
        if(profile!=None):
            cv2.cv.PutText(cv2.cv.fromarray(img),"Name: " + str(profile[1]),(x,y+h),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img),"Address:" + str(profile[2]),(x,y+h+30),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img),"Gender:" + str(profile[3]),(x,y+h+60),font,255)
            cv2.cv.PutText(cv2.cv.fromarray(img),"Work:" + str(profile[4]),(x,y+h+90),font,255)
    cv2.imshow('Face',img)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
