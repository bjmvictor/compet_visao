# M3 - Keypoints

## Entregas esperadas

Artefato: um relatório de meia página com: a taxa de detecção obtida, o que mudou após regravar (se precisou) e uma observação sobre a qualidade dos keypoints. Classroom

#### Critério de aceite:
- Relata a taxa de detecção final.
- Se abaixo de 90%, mostra a tentativa de melhoria (regravação).

## Exercícios realizados

- [x] Regravado um video de experimentação
- [x] Extrair o JSON com os keypoints dos videos gravados
- [x] Comparar a qualidade dos keypoints do video1 com o video2

## Relato

O JSON gerado do primeiro vídeo obteve uma taxa de 64.7% como foi informado na atividade anterior(M3) estando abaixo da meta de 90%. Após regravar utilizando a camera do celular que possui uma qualidade melhor, e utilizando um angulo que melhorasse o fundo foi possivel conseguir 100% da detecção utilizando os mesmos parâmetros mesmo em um vídeo maior (17s).

<figure style="margin: 20px 10px; max-width:800px;">
    <img src=".\files\img\keypoints_video1.jpg" alt="Extração dos keypoints do video 1">
    <figcaption>Extração dos keypoints do video 1</figcaption>
</figure>
<figure style="margin: 20px 10px; max-width:800px;">
    <img src=".\files\img\keypoints_video2.jpg" alt="Extração dos keypoints do video 2">
    <figcaption>Extração dos keypoints do video 2 (regravado)</figcaption>
</figure>

Percebe-se que ao melhorar o enquadramento e utilizar um fundo mais limpo realmente é eficaz para melhorar a precisão da detecção, após regravar aplicando os métodos informados obtive um aumento de 35% na precisão e na qualidade dos keypoints que conseguiram ser identificados corretamente em todos os quadros do video 2
