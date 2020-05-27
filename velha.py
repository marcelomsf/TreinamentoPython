X = "X"
O = "O"
VAZIO = " "
tabuleiro = []
# tabuleiro = [0, 1, 2,
#               3, 4, 5
#               6, 7, 8]

# Horizontal
if tabuleiro[0] == tabuleiro[1] == tabuleiro [2]:
    print("O jogo acabaou")
if tabuleiro[3] == tabuleiro[4] == tabuleiro [5]:
    print("O jogo acabaou")
if tabuleiro[6] == tabuleiro[7] == tabuleiro [8]:
    print("O jogo acabaou")

# Vertical
if tabuleiro[0] == tabuleiro[3] == tabuleiro [6]:
    print("O jogo acabaou")
if tabuleiro[1] == tabuleiro[4] == tabuleiro [7]:
    print("O jogo acabaou")
if tabuleiro[2] == tabuleiro[5] == tabuleiro [8]:
    print("O jogo acabaou")

# Diagonal
if tabuleiro[0] == tabuleiro[4] == tabuleiro [8]:
    print("O jogo acabaou")
if tabuleiro[2] == tabuleiro[4] == tabuleiro [6]:
    print("O jogo acabaou")