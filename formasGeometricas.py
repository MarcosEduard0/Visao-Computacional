import cv2

img = cv2.imread('piramide.jpg')
cv2.rectangle(img, (50, 50), (200, 200), (0, 0, 255), 5)
cv2.circle(img, (200, 200), 80, (255, 0, 0), 5)
cv2.line(img, (400, 400), (500, 400), (0, 255, 0), 2)

texto = 'Estou aprendendo visao'

cv2.putText(img, texto, (200, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)

cv2.imshow('original', img)
cv2.waitKey(0)

video = cv2.VideoCapture('runners.mp4')

while True:
    check, img = video.read()
    cv2.rectangle(img, (50, 50), (200, 200), (0, 0, 255), 5)
    cv2.circle(img, (200, 200), 80, (255, 0, 0), 5)
    cv2.line(img, (400, 400), (500, 400), (0, 255, 0), 2)

    texto = 'Estou aprendendo visao'

    cv2.putText(img, texto, (200, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)

    cv2.imshow('original', img)
    cv2.waitKey(10)
