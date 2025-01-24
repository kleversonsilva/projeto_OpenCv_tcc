#RECONNHECIMENTO DA FACE1

import cv2

carregaAlgoritmo= cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml') #carregar o arquivo xml-daPasta_haacacade
imagem = cv2.imread('fotos/imagem01.jpg') #carregarAimagem rtfffttttttttttttttdctt

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) #Utilizar_aImagem_escala_sinza

faces = carregaAlgoritmo.detectMultiScale(imagemCinza)  #detecçao_das_faces............................................................................
print(faces)

for(x, y, l, a) in faces: #eixo x e y,l==largura, a==altura...Aqui crio o retangulo q aparece na FaceDaimagem
    cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 2)  #define a cor e Borda=(0, 255, 0), 2)


cv2.imshow('faces', imagem)  #mostra a imagem
cv2.waitKey()



