import cv2 as cv

# img= cv.imread('thor.jpg')

# cv.imshow('THOR',img)

def rescaleFrame(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    height= int(frame.shape[0]*scale)

    dimensions= (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

capture= cv.VideoCapture('Instagram.mp4')

while True:
    isTrue, frame= capture.read()

    frame_resized= rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)

