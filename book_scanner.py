import numpy as np #
import cv2  #computer vision for scanning 
import utlis #utils basic library  
import mysql.connector #lets python programs accesss MySQL databases 
from mysql.connector import Error #lets python programs accesss MySQL databases 
import pandas as pd #data structures and oop

from MYSQL_Connector import *

#This file is for the CV2 code that scans the pages and exports the data into MYSQL_Connector


#Used Document Scanner Open cv python tutorial 
#Initalizing defult parameters 
webCamFeed = True
pathImage = "1.jpg"
cap = cv2.VideoCapture(1)
cap.set(10,160) #setting the brightness of the image 
heightImg = 640 #height and width of image 
widthImg = 480

utlis.initalizeTrackbars()
count = 0

while True:
        imgBlank = np.zeros((heightImg, widthImg,3),np.uint8) #Created a blank image for testing 

        if webCamFeed:success, img = cap.read() 
        else: img = cv2.imread(pathImage)
        img = cv2.resize(img,(widthImg, heightImg)) #resizes the image 