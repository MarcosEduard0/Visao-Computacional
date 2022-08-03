import cv2

classificador = cv2.CascadeClassifier(r'haarcascade_treinamento/cascade.xml')

camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while True:
    ret, img = camera.read()

    imgGrey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    objetos = classificador.detectMultiScale(imgGrey, scaleFactor=1.2)

    if not len(objetos):
        pass
    if len(objetos):
        for (x, y, l, a) in objetos:
            cv2.rectangle(img, (x, y), (x+l, y+a), (255, 0, 0), 2)

    cv2.imshow('camera', img)
    cv2.waitKey(1)
