#Capta Olhos e rosto__GPT- OK

import cv2

carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('fotos/imagem01.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#scaleFactor de 1.08 significa___que a imagem é reduzida em 8% a cada iteração.
#minNeighbors = 9: Este parâmetro___especifica quantos "vizinhos" cada retângulo candidato a face deve
# ter para ser considerado uma detecção válida. "Vizinhos" são outros retângulos detectados próximos
# ao retângulo atual.
#Valores maiores (ex: 6, 8, 10 ou como no seu caso 9) ajudam a reduzir falsos positivos, ou seja,
# detecções incorretas de objetos que não são faces

faces = carregaFace.detectMultiScale(imagemCinza, scaleFactor = 1.3, minNeighbors=8) # Ajuste dos parâmetros

for (x, y, l, a) in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)
    roi_cinza = imagemCinza[y:y + a, x:x + l] # Correção importante: usar a imagem em tons de cinza original
    roi_cor = imagem[y:y + a, x:x + l] # Região de interesse na imagem colorida

    olhos = carregaOlho.detectMultiScale(roi_cinza) # Detecta olhos na região de interesse em cinza

    for (ox, oy, ol, oa) in olhos:
        cv2.rectangle(roi_cor, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2) # Desenha o retângulo na imagem colorida

cv2.imshow("Detecta Face e Olhos ", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

