import cv2
import numpy as np
import sqlite3

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
detector = cv2.CascadeClassifier('face.xml')
cap = cv2.VideoCapture(0)

def insertOrUpdate(Id,name):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Persons WHERE ID =" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist==1:
        cmd = cmd="UPDATE Persons SET Name=' "+str(name)+" ' WHERE ID="+str(Id)
        # conn.execute(cmd)
    else:
        cmd="INSERT INTO Persons(ID,Name) Values("+str(Id)+",' "+str(name)+" ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()


id = raw_input()
name = raw_input("Enter Your name:\n")
# address = raw_input()

insertOrUpdate(id,name)
sampleNum = 0

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + "." + str(name) + ".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow('Face',img)
    if(sampleNum>20):
        break

cap.release()
cv2.destroyAllWindows()
