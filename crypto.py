# abacaxi
#
# a - d
# b - e
# c - f
# x - a
# i -l
#
# dedfdal

alfabeto = ['a', 'b', 'c', 'd' , 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm'
            'n', 'o', 'p', 'q', 'r', 's', 't' ,'u', 'v','w', 'x', 'y', 'z']
tamanho_alfabeto = len(alfabeto)
chave = 3
mensagem = "abacaxi"
cifrada = ""
for letra in mensagem:
    print(letra)
    indice = alfabeto.index(letra)
    nova_letra = alfabeto[(indice + chave)%tamanho_alfabeto]
    cifrada = cifrada + nova_letra

print(mensagem)
print(cifrada)