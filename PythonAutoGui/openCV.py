import cv2

#show img details (array int 3d)
img = cv2.imread("image/cat.jpg") #transform img to array 3d
imgResize = cv2.resize(img, (600, 600))
imgRecolor = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
print(img)

#show img

cv2.imshow("outpout", imgRecolor)
cv2.waitKey(0) #define the times to show images by millisec (if 0, it'll still be there til you close)
cv2.destroyAllWindows()

#save img
cv2.imwrite("catTestSavel.png", imgRecolor)