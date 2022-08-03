import cv2

camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)

amostra = 1

while True:
    ret, img = camera.read()
    imgGrey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        imgR = cv2.resize(imgGrey, (220, 220))
        cv2.imwrite(
            f'haarcascade_treinamento/fotos/positivo/im{amostra}.jpg',  imgR)
        amostra += 1

    cv2.imshow('Captura', img)
    cv2.waitKey(1)
