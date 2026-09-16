import cv2                        # OpenCV: abrir e inspecionar o vídeo
import numpy as np              # NumPy: cálculos sobre os quadros (matrizes)
import matplotlib.pyplot as plt # matplotlib: exibir quadros no notebook

VIDEO = r"./files/video.mp4"

def mostrar(imagem, titulo=""):
    rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # BGR (OpenCV) -> RGB (matplotlib)
    plt.imshow(rgb)             # desenha a imagem
    plt.title(titulo)           # título
    plt.axis("off")             # esconde eixos
    plt.show()                  # renderiza

def gerar_amostra_video(CAMINHO_VIDEO):
    # Gera um vídeo de ~12 s (fundo cinza claro, um retângulo simulando a "mão")
    fps = 10                                 # quadros por segundo
    larg, alt = 640, 480                     # resolução (largura, altura)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v") # codec para arquivo .mp4
    esc = cv2.VideoWriter(
        "exemplo_captura.mp4",               # arquivo de saída
        fourcc,                              # codec
        fps,                                # taxa de quadros
        (larg, alt),                        # frameSize (largura, altura)
    )
    for i in range(120):                     # 120 quadros / 10 fps = 12 s
        q = np.full((alt, larg, 3), 150, dtype=np.uint8)  # fundo cinza (150 = boa iluminação)
        x = 60 + i                            # posição que muda (simula movimento)
        cv2.rectangle(q, (x, 200), (x + 120, 320), (90, 120, 200), -1)  # "mão"
        esc.write(q)                          # grava o quadro
    esc.release()                            # finaliza o arquivo
    print("vídeo de exemplo criado")

def medir_video(CAMINHO_VIDEO):
    cap = cv2.VideoCapture(CAMINHO_VIDEO)          # abre o vídeo (caminho do arquivo)
    assert cap.isOpened(), "Não consegui abrir o vídeo"  # para se falhar

    fps_v = cap.get(cv2.CAP_PROP_FPS)              # quadros por segundo
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # total de quadros
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))     # largura (pixels)
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    # altura (pixels)
    duracao = total / fps_v if fps_v else 0        # duração em segundos = quadros / fps
    print(f"fps={fps_v} | quadros={total} | resolução={w}x{h} | duração={duracao:.1f}s")

    # Pega 3 quadros igualmente espaçados (início, meio, fim) para inspeção visual
    indices = [int(total * f) for f in (0.1, 0.5, 0.9)]  # posições relativas
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx)     # posiciona o leitor no quadro idx
        ok, q = cap.read()                        # lê aquele quadro
        if ok:                                     # se leu com sucesso
            mostrar(q, f"Quadro {idx}")           # exibe

    # Media de luminosidade
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)           # volta ao início
    brilhos = []                                   # brilho médio de cada quadro
    while True:
        ok, q = cap.read()                         # lê um quadro
        if not ok:                                 # fim do vídeo
            break
        cinza = cv2.cvtColor(q, cv2.COLOR_BGR2GRAY)  # brilho = imagem em cinza
        brilhos.append(float(np.mean(cinza)))      # média de todos os pixels
    cap.release()                                  # libera o arquivo

    brilho_medio = float(np.mean(brilhos))         # brilho médio do vídeo inteiro
    print(f"brilho médio: {brilho_medio:.1f} (ideal: entre ~60 e ~200)")
    plt.plot(brilhos)                              # curva de brilho ao longo do tempo
    plt.xlabel("quadro"); plt.ylabel("brilho (0-255)"); plt.title("Iluminação ao longo do vídeo")
    plt.show()

    # Checklist de qualidade em relação ao protocolo de captura
    check("Duração entre 10 e 20 s", 10 <= duracao <= 20)      # duração no intervalo pedido
    check("Resolução mínima 480p (altura >= 480)", h >= 480)    # resolução adequada
    check("Iluminação adequada (brilho 60-200)", 60 <= brilho_medio <= 200)  # nem escuro, nem estourado
    print("\nSe algum item deu ATENÇÃO, regrave ajustando o ponto indicado.")

# Checar se o video atende ao protocolo de captura
def check(nome, condicao):                      # imprime PASSOU/ATENÇÃO para cada critério
    print(("✔ " if condicao else "✗ ATENÇÃO: ") + nome)

#gerar_amostra_video(VIDEO)
medir_video(VIDEO)