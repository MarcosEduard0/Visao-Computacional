import cv2

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()
    # print(img.shape)
    imgRedim = cv2.resize(img, (640, 420))
    cv2.imshow('Video', imgRedim)
    cv2.waitKey(0)
