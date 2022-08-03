import cv2

camera = cv2.VideoCapture(0)
camera.set(3, 640)  # largura
camera.set(4, 420)  # altura
camera.set(10, 400)  # brilho/ luminosiade

while True:
    check, img = camera.read()

    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
