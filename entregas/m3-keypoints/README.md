# M3 - Keypoints

## Entregas esperadas

Artefato: o keypoints.json do seu vídeo + 3 frases explicando o que há dentro dele (o que é metadata e o que são os frames).

#### Critério de aceite:
- JSON gerado com sucesso.
- Você identifica onde estão a taxa de detecção e os landmarks.
- Arquivo registrado no Classroom.

## Exercícios realizados

- [] Gerar um JSON dos frames com mão
- [] Explicar o conteudo do JSON
- [x] Executar o detector com o modelo hand_landmarker.task

## Relato

Link do modelo utilizado: [Google Developers HandLandmarker](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/index#models)

Durante a execução do detector, houve falha algumas vezes na quantidade correta de mãos, mas ao ajustar o parâmetro de ´´´min_hand_detection_confidence´´´ foi possivel obter uma melhor precisão na detecção.

<img src=".\files\img\hand-detection1.jpg" alt="Imagem exibindo a detecção de mão falha" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\hand-detection2.jpg" alt="Imagem exibindo a detecção de mão melhorada após ajuste de parâmetro" style="margin: 10px auto; max-width:800px;">
