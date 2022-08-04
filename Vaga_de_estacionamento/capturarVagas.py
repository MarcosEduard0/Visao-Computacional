import cv2
import pickle

img = cv2.imread('Vaga_de_estacionamento/estacionamento.png')


vagas = []
for x in range(69):  # temos 69 vagas
    vaga = cv2.selectROI('vagas', img, False)
    cv2.destroyWindow('vagas')
    vagas.append((vaga))

    for x, y, w, h in vagas:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

with open('Vaga_de_estacionamento/vagas.pkl', 'wb') as arquivo:
    pickle.dump(vagas, arquivo)
