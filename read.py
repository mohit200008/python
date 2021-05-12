import cv2 as cv 

img = cv.imread('thor.jpg')

cv.imshow('Thor', img)

cv.waitKey(0)