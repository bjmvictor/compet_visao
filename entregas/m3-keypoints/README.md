# M3 - Keypoints

## Entregas esperadas

Artefato: o keypoints.json do seu vídeo + 3 frases explicando o que há dentro dele (o que é metadata e o que são os frames).

#### Critério de aceite:
- Artefato: texto explicando oque é o keypoints.json, metadada e frames.
- JSON gerado com sucesso.
- Você identifica onde estão a taxa de detecção e os landmarks.
- Arquivo registrado no Classroom.

## Exercícios realizados

- [x] Gerar um JSON dos frames com mão
- [x] Explicar o conteudo do JSON
- [x] Executar o detector com o modelo hand_landmarker.task

## Relato

O JSON gerado exibe que o total de frames que foi localizado mão foram 196 frames de 303 totais, que deu 64,7% oque é compreensivel porque o meu vídeo não apresenta 100% da mão o tempo inteiro.

Durante a execução do detector manual em algumas imagens de mãos, houve algumas falhas na quantidade correta de mãos, mas ao ajustar o parâmetro de ´´´min_hand_detection_confidence´´´ foi possivel obter uma melhor precisão na detecção.

Link do modelo utilizado no teste manual: [Google Developers HandLandmarker](https://developers.google.com/edge/mediapipe/solutions/vision/hand_landmarker/index#models)

<img src=".\files\img\hand-detection1.jpg" alt="Imagem exibindo a falha na detecção de mão" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\hand-detection2.jpg" alt="Imagem exibindo a detecção de mão melhorada após ajuste de parâmetro" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\frames_extract.png" alt="Frames extraidos do video para gerar o JSON" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\hand_keypoints.png" alt="Keypoints de mão extraidos do vídeo" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\distance_ind_punho.png" alt="Distancia do indicador até o punho" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\json_analyze_output.png" alt="Analise realizada no JSON extraido" style="margin: 10px auto; max-width:800px;">