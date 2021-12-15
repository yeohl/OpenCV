import cmake as cmake
import cv2
import numpy as np
import face_recognition
import os

path = 'face_images'
images = []
KnownNames = []
KnownFaces = os.listdir(path)
print(KnownFaces)
for cl in KnownFaces:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    KnownNames.append(os.path.splitext(cl)[0])
print(KnownNames)

imgKim = face_recognition.load_image_file('face_images/Kim.jpg')
imgKim = cv2.cvtColor(imgKim.cv2.COLOR_BGR2RGB)
imgHee = face_recognition.load_image_file('face_images/Heejin.jpg')
imgHee = cv2.cvtColor(imgHee.cv2.COLOR_BGR2RGB)
imgJin = face_recognition.load_image_file('face_images/Jin.jpg')
imgJin = cv2.cvtColor(imgJin.cv2.COLOR_BGR2RGB)
