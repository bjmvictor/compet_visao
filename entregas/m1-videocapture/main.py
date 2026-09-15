import cv2
import numpy as np

video = r'./files/video-10s.mp4'

cap = cv2.VideoCapture(video)

# Dados do video
totalQuadros = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
quadroMeio = totalQuadros // 2

cap.set(cv2.CAP_PROP_POS_FRAMES, quadroMeio) #Define o quadro que será lido

ok, meio = cap.read()

if ok:
    cv2.imwrite('meio.jpg', meio)

cap.release()

# ler a imagem salva para extrair os dados
img = cv2.imread('meio.jpg')

print(f"""
      Total de frames: {totalQuadros}
      FPS: {fps}
      Tamanho da imagem: {largura * altura} pixels ( {largura} x {altura} )
      Canais: {img.shape[2]}
      """)


## Extra 1: Salve todos os quadros em uma pasta frames/
frames_dir = r'frames/'

cap2 = cv2.VideoCapture(video)

totalFrames = cap2.get(cv2.CAP_PROP_FRAME_COUNT)
_, frame = cap2.read()

for i in range(int(totalFrames)):
    cv2.imwrite(f"{frames_dir}{i:03d}.jpg", frame)
    print(f"Salvo o frame {i} em: {frames_dir}{i:03d}.jpg")


## Extra 2: Converter o quadro do meio para escala de cinza e detectar bordar com Canny
gray = cv2.imread('meio.jpg', cv2.IMREAD_GRAYSCALE)
canny = cv2.Canny(gray, 50, 150)
cv2.imwrite('gray.jpg', gray)
cv2.imwrite('canny.jpg', canny)

## Extra 3: Descobrir a duração do video em segundos
duracaoSegundos = totalFrames / fps
print(f"\nDuração do vídeo em segundos: {duracaoSegundos}s")