import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import pandas
import pygame
import time
import serial
# Initialize pygame mixer
pygame.mixer.init()
s = serial.Serial('COM7',9600)
# Function to play the alarm sound
def play_alarm():
    alarm_sound = pygame.mixer.Sound('alarm.wav')
    alarm_sound.play()

# Function to stop the alarm sound+
def stop_alarm():
    pygame.mixer.stop()

model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp6/weights/last.pt',source='local', force_reload=True)
cap = cv2.VideoCapture(0)
score=0
while cap.isOpened():
    ret, frame = cap.read()
    # Make detections 
    results = model(frame)
    
    df=results.pandas().xyxy[0]
    # print(df)
    if df.empty:
        # print("NOT Detected",end=" ")
        dectect='null'
    else:
        dectect=df.at[0,"name"]
        # print(dectect,end=" ")

    #Sending Info to aurdino
    if(dectect=="drowsy"):
        score+=1
        if(score>=4):
            # play_alarm()
            s.write('1'.encode())
    elif(dectect=='null'):
        score=0
        s.write('2'.encode())
    else:
        score=0
        # stop_alarm()
        s.write('0'.encode())
    # print(score)

    #Show Frame in image
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    #Key for Exit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
    # time.sleep(0.5)
cap.release()
cv2.destroyAllWindows()