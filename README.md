Configurações de importação de bibliotecas. pyfiglet foi usado para estilização de título, e termcolor para coloração do título.
Listas para armazenar caracteres representativos das embarcações, das coordenadas de linhas (letras) e colunas(números).
![Captura de Tela (245)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/6d65c221-5547-4d28-a372-83b42233dbf3)


O jogo consiste em 2 dificuldades: FÁCIL e SURVIVOR, definidas pela variável difficulty:
![Captura de Tela (243)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/8e472890-f30c-454c-b68b-c6be81f4968f)

![ex8_GIF](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/0ff5a074-632f-420c-97e3-38f9aaeb0a66)


E 2 tipos de tabuleiro. A função  definir_tamanho_matriz() definirá o valor das variáveis glboais "linha" e "coluna" para definir o tamanho. 

![ex9_GIF](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/72dbb358-d4d9-4ded-89d7-1c2f6c711bf8)

![Captura de Tela (242)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/e59dfbb7-57c5-48c6-a34f-d29aa49c52d5)


Em seguida, o usuário deverá informar as coordenadas das respectivas embarcações:

![ex10_GIF](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/3369a0bd-cd28-4d19-9e14-4db42f76e2d8)

O terminal irá então printar os tabuleiros do jogador e computador, mostrando o total de embarcações escondidas em cada tabuleiro

![Captura de Tela (239)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/ab99be7c-59cf-4bf2-b833-8608017378e8)

Na rodada do jogador, ele informa as coordenadas para atirar no tabuleiro adversário. O jogo informe se ele acertou ou não. O mesmo vale para o computador, porém as coordenadas serão randomizadas.

![Captura de Tela (240)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/01965ee0-6e6e-4053-a8fb-1d488e203b0e)

Os tabuleiros então são atualizados, mostrando os acertos e erros, e o total de barcos é atualizado:

![ex11_GIF](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/646d949d-d117-4214-8fd8-cf05f0c8272c)

Caso jogador ou computador afunde todas as embarcações do adversário, o jogo dará uma mensagem de parabenização e mostrará os créditos dos desenvolvedores:

![Captura de Tela (241)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/38c7a4fb-1e54-4f19-998f-53b9f52a6dcc)


Funções responsáveis por converter um caractere alfabético em numérico, e vice-versa:
![Captura de Tela (244)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/89589bb2-6861-4241-9299-b0c30032919c)


Ao entrar na condição da dificuldade selecionada, linha e coluna vão receber os valores retornados pela função definir_tamanho_matriz().


A variável build_turn definirá qual matriz será criada primeira


Variáveis recebem nome das embarcações. Valores correspondem ao tamanho delas.
![Captura de Tela (246)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/6bbb17c3-09f1-4781-9f7c-374b4808e044)


A função verificacaoPlayer() será responsável por fazer o usuário e computador informarem as coordendas e horientação (horizontal ou vertival) da embarcação a ser posicionada.

![Captura de Tela (247)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/31149f22-e2f8-4480-90ee-c0ad9d0fcd16)


Cria a matriz que será usada como base para posicionar e verificar as jogadas. Não será vista pelo usuário.

![Captura de Tela (248)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/695ad4e2-2f7c-43db-9e15-ff9ab96df643)


Cria a matriz que iria ser visualizada pelo usuário como um tabuleiro. Inicialmente vazia.

![Captura de Tela (249)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/dec498bf-96f9-4517-8265-2779b75e9972)


Função responsável por atacar os barcos inimigos. O usuário informa as coordenadas, e ocorre a verificação. Se a coordenada corresponde a algum dos caracteres correspondentes ás embarcações ("ANCSD"), o jogador/computador acertou. Caso a coordenada corresponda a '-', o jogador/computador errou.

![Captura de Tela (251)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/7d31f3b8-a64d-45f5-8f8d-08aa18bb1123)



Desenha o tabuleiro na tela, agora levando em conta os barcos escondidos. Mostra os icones de acerto e erro.
![Captura de Tela (250)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/9a92e5f4-b607-4456-9327-a77ebead1ad5)



Define o turno jogador/computador. Por padrão, O jogador é o primeiro (definido na variável 'starts'). A função atirar() então é chamada para executar o ataque contra o adversário. Após a variável starts é atualizada, passando o turno para o adversário.
![Captura de Tela (252)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/6eefc5c9-1976-4c6e-a0a5-30cf18fb7634)


Calcula a pontuação de cada jogador. Primeiro verifica o turno de quem está jogando, então verifica as coordenadas atingidas, diminuindo em 1 o tamanho restante da embarcação inimiga. Se o jogador/ computador atingiu a embracação por inteira, o total de barcos inimigos é diminuido em 1.
![Captura de Tela (253)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/04bac498-8061-45b7-acb5-893c190fd26f)

As seguintes variáveis (matriz_10 e matriz_20) recebem as matrizes criadas. Já as matrizes d1 e d2 armazenam as matrizes visuais (printadas na tela). 
![Captura de Tela (254)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/d3db26e3-cd3a-4621-879a-aa3651f0b169)

Função rodar() irá sempre imprimir as matrizes atualizadas, quando chamada.
![Captura de Tela (255)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/cee41faa-f5b6-47b5-9098-6ff43ebca9f5)


Loop principal do jogo, em que chamará as funções que desencadearão todas a lógica do jogo, além de verificar a pontuação.
![Captura de Tela (256)](https://github.com/VictorFadel06/batalha-Naval/assets/127444074/e557fb48-7dd2-44cf-bd7f-828c8a11ba0a)
