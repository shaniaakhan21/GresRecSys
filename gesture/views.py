from django.shortcuts import render
from .models import Team
from django.conf import settings
from .apps import GestureConfig
from rest_framework.decorators import api_view

import cv2
import matplotlib.pyplot as plt 
from keras.models import load_model
import time
import copy 
import numpy as np
import copy
# import tensorflow as tf

def index(request):
    return render(request, 'index.html')

def front(request):
    return render(request, 'front.html')

def contact(request):
    return render(request, 'contact.html')

@api_view(["POST"])
def reco(request):
        newmodel = load_model('gesture_model1.h5')
        cap = cv2.VideoCapture(0)
        while True:

            ret, frame = cap.read()
            img = copy.deepcopy(frame)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #     faces = face_cascade.detectMultiScale(gray,scaleFactor =  1.3,minNeighbors =  5)
            text = 'Keep your Hand in the box..'
            cv2.putText(img, text, (100, 320),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.rectangle(img, (0,0), (300, 90), (0,0,0), -1)
            cv2.rectangle(img, (100,100), (300, 300), (0,0,255), 2)
            gray = cv2.GaussianBlur(gray,(5,5),0)
            fc = gray[100:300, 100:300]
            roi = cv2.resize(fc, (48,48))

            cv2.imshow('gray',roi)
            time.sleep(0.1)
            pred = newmodel.predict(roi[np.newaxis, :, :, np.newaxis])
            
            text_idx=np.argmax(pred)
            text_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q',
                        'R','S','T','U','Unknown','V','W','X','Y','Z']
            
            if text_idx == 0:
                text1= text_list[0]
            if text_idx == 1:
                text1= text_list[1]
            elif text_idx == 2:
                text1= text_list[2]
            elif text_idx == 3:
                text1= text_list[3]
            elif text_idx == 4:
                text1= text_list[4]
            elif text_idx == 5:
                text1= text_list[5]
            elif text_idx == 6:
                text1= text_list[6]
            elif text_idx == 7:
                text1= text_list[7]
            elif text_idx == 8:
                text1= text_list[8]
            elif text_idx == 9:
                text1= text_list[9]
            elif text_idx == 10:
                text1= text_list[10]
            elif text_idx == 11:
                text1= text_list[11]
            elif text_idx == 12:
                text1= text_list[12]
            elif text_idx == 13:
                text1= text_list[13]
            elif text_idx == 14:
                text1= text_list[14]
            elif text_idx == 15:
                text1= text_list[15]
            elif text_idx == 16:
                text1= text_list[16]
            elif text_idx == 17:
                text1= text_list[17]
            elif text_idx == 18:
                text1= text_list[18]
            elif text_idx == 19:
                text1= text_list[19]
            elif text_idx == 20:
                text1= text_list[20]
            elif text_idx == 21:
                text1= text_list[21]
            elif text_idx == 22:
                text1= text_list[22]
            elif text_idx == 23:
                text1= text_list[23]
            elif text_idx == 24:
                text1= text_list[24]
            elif text_idx == 25:
                text1= text_list[25]
            elif text_idx == 26:
                text1= text_list[26]
            cv2.putText(img, text1, (10,60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255,255), 3)
            cv2.imshow("frame", img)
            key = cv2.waitKey(1) & 0xFF
            if key== ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        return render(request, 'camera.html')