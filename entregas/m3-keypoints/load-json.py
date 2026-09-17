import json, random, math
import matplotlib.pyplot as plt
import cv2, numpy as np, math

with open("keypoints.json", encoding="utf-8") as f:  # troque pelo seu keypoints.json
    kp = json.load(f)                     # carrega o JSON como dicionário

print("Chaves do topo:", list(kp.keys()))            # 'metadata' e 'frames'
print("Metadata:", kp["metadata"])                    # info do vídeo e da extração
print("Nº de quadros:", len(kp["frames"]))            # tamanho da lista de quadros
print("Exemplo de quadro (chaves):", list(kp["frames"][0].keys()))  # frame, hands, pose

##--------------------------------------------------------------------------------------------------------##
## Procura o primeiro quadro que tenha mão detectada
##--------------------------------------------------------------------------------------------------------##
quadro_com_mao = next(f for f in kp["frames"] if f["hands"])  # 1º com lista de mãos não vazia
mao = quadro_com_mao["hands"][0]           # a primeira mão do quadro
lms = mao["landmarks"]                      # os 21 landmarks
print("mão:", mao["hand"], "| nº de landmarks:", len(lms))
print("punho (0):", lms[0])                 # coordenadas normalizadas (0..1)
print("ponta do indicador (8):", lms[8])

##--------------------------------------------------------------------------------------------------------##
## Desenhar os keypoints em um quadro
##--------------------------------------------------------------------------------------------------------##
W, H = 320, 240                             # tamanho do "canvas" para desenhar
canvas = np.zeros((H, W, 3), dtype=np.uint8)  # imagem preta

for p in lms:                               # para cada landmark da mão
    x = int(p["x"] * W)                     # x normalizado -> pixel (coluna)
    y = int(p["y"] * H)                     # y normalizado -> pixel (linha)
    cv2.circle(
        canvas,                             # imagem onde desenhar
        (x, y),                             # centro do ponto (x, y)
        3,                                  # raio do ponto (pixels)
        (0, 255, 0),                        # cor BGR: verde
        -1,                                 # -1: preenchido
    )
plt.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))  # BGR->RGB p/ exibir
plt.title("21 keypoints da mão"); plt.axis("off"); plt.show()

##--------------------------------------------------------------------------------------------------------##
## primeira feature: distancia indicador-punho
##--------------------------------------------------------------------------------------------------------##
def dist(a, b):                             # distância euclidiana entre 2 landmarks
    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])  # hypot = sqrt(dx^2 + dy^2)

serie = []                                  # distância por quadro (quando há mão)
for f in kp["frames"]:                       # percorre todos os quadros
    if f["hands"]:                           # só quando há mão detectada
        l = f["hands"][0]["landmarks"]       # landmarks da 1ª mão
        serie.append(dist(l[8], l[0]))       # distância indicador(8) - punho(0)
plt.plot(serie)                              # evolução da feature no tempo
plt.xlabel("quadro (com mão)"); plt.ylabel("distância normalizada")
plt.title("Feature: distância indicador–punho"); plt.show()
print("distância média:", round(sum(serie) / len(serie), 4))

##--------------------------------------------------------------------------------------------------------##
## Taxa de detecção
##--------------------------------------------------------------------------------------------------------##
com_mao = sum(1 for f in kp["frames"] if f["hands"])  # quadros com mão
total = len(kp["frames"])                              # total de quadros
print(f"quadros com mão: {com_mao}/{total} = {100*com_mao/total:.1f}%")
print("hand_detection_rate (metadata):", kp["metadata"]["hand_detection_rate"])