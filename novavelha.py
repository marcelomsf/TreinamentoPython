X = "X"
O = "O"
VAZIO = " "
TAMANHO_TABULEIRO = 9


# tabuleiro = [0, 1, 2,
#               3, 4, 5
#               6, 7, 8]

tabuleiro = []
tabuleiro = [VAZIO, VAZIO, VAZIO,
            VAZIO, VAZIO, VAZIO,
            VAZIO, VAZIO,VAZIO]
jogada = 0
jogo_valido = True
vencedor = False
marcador_valido = False

jogador1 = VAZIO
jogador2 = VAZIO
while not marcador_valido:
    jogador1 = input("Escolha X ou O: ")
    if jogador1 == X or jogador1 == O:
        marcador_valido = True
    else:
        print("Opção invalida escolhida")

if jogador1 == X:
    jogador2 = O
else:
    jogador2 = X

for i in range(0, 9, 3):
    print(i, "|", i+1, "|", i+2, "      ",tabuleiro[i], "|", tabuleiro[i+1],"|", tabuleiro[i+2])

while jogo_valido:
    jogada = jogada + 1
    casa = int(input("Escolha onde jogar: "))

    if ( tabuleiro[casa] == VAZIO ):
        if jogada%2 == 1:
            tabuleiro[casa] = jogador1
        else:
            tabuleiro[casa] = jogador2
    else:
        print("Joga invalida, casa já marcada")
        jogada = jogada - 1

    for i in range(0, 9, 3):
        print(i, "|", i+1, "|", i+2, "      ",tabuleiro[i], "|", tabuleiro[i+1],"|", tabuleiro[i+2])

    # Horizontal
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro [i+2] != VAZIO:
            vencedor = tabuleiro[i]

    # Vertical
    if not vencedor:    
        for i in range(0,3):
            if tabuleiro[i] == tabuleiro[i+3] == tabuleiro [i+6] != VAZIO:
                vencedor = tabuleiro[i]

    # Diagonal
    if not vencedor:
        for i in range(0, 3, 2):
            if tabuleiro[0+i] == tabuleiro[4] == tabuleiro [8-i] != VAZIO:
                vencedor = tabuleiro[i]


    # Final do Jogo
    if vencedor:
        print("Vencedor: ",vencedor)
        jogo_valido = False
    else:
        if not VAZIO in tabuleiro:
            print("Jogo empatou: Deu velha")
            jogo_valido = False


