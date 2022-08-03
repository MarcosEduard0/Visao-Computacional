import cv2

# camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
camera = cv2.VideoCapture('haarcascade/video.mp4')

classificador = cv2.CascadeClassifier(
    # r'haarcascade/cascades/haarcascade_eye.xml')
    # r'haarcascade/cascades/haarcascade_frontalface_default.xml')
    # r'haarcascade/cascades/haarcascade_smile.xml')
    r'haarcascade/cascades/haarcascade_fullbody.xml')

while True:
    check, img = camera.read()
    img = cv2.resize(img, (1280, 960))

    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(
        imgGrey, minSize=(50, 50), scaleFactor=1.5)
    # print(objetos)

    for x, y, l, a in objetos:
        cv2.rectangle(img, (x, y), (x+l, y+a), (255, 0, 0), 2)

    cv2.imshow('teste', img)
    cv2.waitKey(10)
