import cv2
import numpy as np
import time
import mysql.connector as mariadb
import datetime


cap = cv2.VideoCapture(0)

class Data:
    __revolutions = 0
    __start = 0
    __end = 0
    __id = 0
    def __init__(self, revolutions, start, end, id_):
        self.__revolutions = revolutions
        self.__start = start
        self.__end = end
        self.__id_ = id_
    def sendToServer(self):
        mariadb_connection = mariadb.connect(host='qpartys.de', user='testuser', password='12345', database='test')
        cursor = mariadb_connection.cursor()

        detectValue = 0
        cursor.execute("INSERT INTO kittyspinny (revolutions, start, end, catId) VALUES (%s)", (self.__revolutions, self.__start, self.__end, self.__id,))
        mariadb_connection.commit()
        cursor.close()
    def setId(self, input_):
        self.__id = input_
    def setRevolution(self,input_):
        self.__revolutions = input_
    def setStartTime(self, input_):
        self.__start = input_
    def setEndTime(self, input_):
        self.__end = input_
        
    def getId(self):
        print(self.__id)


def Found(color): 
    print(color)
    if color=="red":
        Data.setId(data,1)
        Data.getId(data)
    elif color=="yellow":
        Data.setId(data,0)
        Data.getId(data)

def Detect():
    found = False
    # Red color
    low_red = np.array([160, 150, 80])
    high_red = np.array([180, 255, 255])
    # Yellow color
    low_yellow = np.array([20,100,100])
    high_yellow = np.array([30,255,255])
    
    low = [low_yellow, low_red]
    high = [high_yellow, high_red]
    while True:
        ret, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Mask for red
#        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
#        red = cv2.bitwise_and(frame, frame, mask = red_mask)     
        # Mask for yellow
#        yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
#        yellow = cv2.bitwise_and(frame, frame, mask = yellow_mask)
        
        if ret==True:
            for i in [0,1]:
                mask = cv2.inRange(hsv_frame, low[i], high[i])
                color = cv2.bitwise_and(frame, frame, mask = mask)
#                _,contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                _,contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                
                for c in contours:
                    if cv2.contourArea(c) > 3000:
#                        cv2.drawContours(red,c,-1,(255,255,0),1)
                        cv2.drawContours(color,c,-1,(255,255,0),1)
                        Found(i)
                        found = True
        if found:
            break

#        key = cv2.waitKey(1)
#        if key == 27:
#            break
def WheelStart():
    pass

data = Data(0, 0, 0, 0)
Detect()
