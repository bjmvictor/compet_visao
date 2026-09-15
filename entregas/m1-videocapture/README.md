# M1 - OpenCV Imagem e Video

## Entregas esperadas

Reúna o que praticou em um script .py no seu branch, que:

- abra um vídeo,
- conte os quadros,
- salve o quadro do meio como imagem,
- e traga um comentário de 1–2 frases explicando como o vídeo é representado (pixels, canais, fps).

| Critério de aceite: o script roda sem erro e imprime o total de quadros; gera a imagem do quadro do meio; e está commitado no seu branch pessoal.

## Desafios extras (opcionais)

- Salve todos os quadros em uma pasta frames/ (dica: cv2.imwrite(f"frames/{i:03d}.jpg", q)).
- Converta o quadro do meio para escala de cinza e detecte bordas com Canny.
- Descubra a duração do vídeo em segundos (dica: total_de_quadros / fps).

## Exercícios realizados

- [x] Abra um vídeo.
- [x] Conte os quadros.
- [x] Salve o quadro do meio como imagem.
- [x] Traga um comentário de 1–2 frases explicando como o vídeo é representado (pixels, canais, fps).
#### Extra:
- [x] Salve todos os quadros em uma pasta frames/ (dica: cv2.imwrite(f"frames/{i:03d}.jpg", q)).
- [x] Converta o quadro do meio para escala de cinza e detecte bordas com Canny.
- [x] Descubra a duração do vídeo em segundos (dica: total_de_quadros / fps).

## Relato

Durante a implementação dessa atividade proposta, tive dificuldades com relação ao uso de memória. No inicio pensei em obter e salvar todos os frames em uma única lista e fiz o algoritmo para isso, entretanto mesmo com vídeos pequenos de 10s, 5s, 3s ainda continuava consumindo muita memoria chegando até a um erro por memoria insuficiente.

Pensei em outra estratégia mas não sabia se era possível obter o total de frames e carregar um frame em específico e ao pesquisar descobri que era possível, após isso implementei esse algoritmo que pega o total de frames sem precisar iterar em um loop, e pegando o index do centro e utilizando-o como parâmetro para o OpenCV foi possivel extrair o frame do meio do vídeo, salvar como imagem e alterar as configurações de cor com o mínimo de uso da memória.

<img src=".\files\img\memory_use.jpg" alt="Imagem exibindo excesso de uso da memoria RAM" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\memory_error.jpg" alt="Exibição do erro por falta de memoria RAM" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\console_out.jpg" alt="Saida do console final" style="margin: 10px auto; max-width:800px;">
<img src=".\files\img\fullscreen_end.jpg" alt="Tela completa da IDE exibindo as imagens extraidas do vídeo" style="margin: 10px auto; max-width:800px;">
