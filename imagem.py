import cv2
from cv2 import selectROI


# Cortar uma imagem
img = cv2.imread('farol.jpg')
dim = cv2.selectROI("Selecione a area de recorte", img, False)
v1, v2, v3, v4 = int(dim[0]), int(dim[1]), int(dim[2]), int(dim[3])

recorte = img[v2:v2+v4, v1:v1+v3]
diretorio = 'recortes/img01.jpg'
cv2.imwrite(diretorio, recorte)
cv2.imshow('Imagem', img)
cv2.imshow('Imagem recorte', recorte)
cv2.waitKey(0)


# # sabendo as dimensoes

# recorte = img[310:520, 120:420]
# cv2.imshow('Imagem', img)
# cv2.imshow('Imagem Recorte', recorte)
# cv2.waitKey(0)


# # Mexendo com imagens

# img = cv2.imread('farol.jpg')
# imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # print(img.shape)
# print(imgCinza)
# cv2.imshow('Imagem', img)
# cv2.imshow('Imagem Cinza', imgCinza)
# cv2.waitKey(0)
