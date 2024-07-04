import cv2
import pyautogui
import numpy as np

screen = pyautogui.screenshot()
img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)

nah = cv2.imread("image/nah.jpg")

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def ToGray(x):
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    return x

grayimg = ToGray(img)
scaleFactor = 1.1
minNeighbor = 10
detact = cascade.detectMultiScale(grayimg, scaleFactor, minNeighbor)

if type(detact) != tuple:
    for (x, y, w, h) in detact:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=5)
    img = cv2.resize(img, (1000,500))
    cv2.imshow("Original", img)
    cv2.waitKey(0)
else : 
    cv2.imshow("NAH", nah)
    cv2.waitKey(0)