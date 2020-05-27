X = "X"
O = "O"
VAZIO = " "
TAMANHO_TABULEIRO = 9
tabuleiro = []

# tabuleiro = [0, 1, 2,
#               3, 4, 5
#               6, 7, 8]

# Horizontal
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro [i+2] != VAZIO:
        print("O jogo acabou")

# Vertical
for i in range(0,3):
    if tabuleiro[i] == tabuleiro[i+3] == tabuleiro [i+6] != VAZIO:
        print("O jogo acabaou")

# Diagonal
for i in range(0, 3, 2):
    if tabuleiro[0+i] == tabuleiro[4] == tabuleiro [8-i] != VAZIO:
        print("O jogo acabaou")
