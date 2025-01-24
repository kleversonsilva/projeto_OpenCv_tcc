
#RECONNHECIMENTO DA FACE2

import cv2

carregaAlgoritmo= cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
imagem = cv2.imread('fotos/image02.jpg') #carregarAimagem

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #Utilizar_aImagem_escala_sinza

faces = carregaAlgoritmo.detectMultiScale(imagemCinza, scaleFactor=1.08, minNeighbors=4, minSize=(35, 35))  #detecçao_das_faces. (caleFactor=diminui a escala. Pode melhrarImagem=minNeighbors=1. OBS: Nesa linhaAjustoOsparametros).....................................................
print(faces)

for(x, y, l, a) in faces: #eixo x e y,l==largura, a==altura...Aqui crio o retangulo q aparece na FaceDaimagem
    cv2.rectangle(imagem, (x, y), (x+l, y+a), (255, 0, 255), 2)  #define a cor e Borda=(0, 255, 0), 2)

cv2.imshow('faces', imagem)  #mostra a imagem
cv2.waitKey()
