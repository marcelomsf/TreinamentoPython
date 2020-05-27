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
#tamanho_alfabeto = len(alfabeto)
tamanho_alfabeto = 128
limite_alfabeto_minisculo=122
limite_alfabeto_maisculo= 90
letras_alfabeto = 26

chave = 3
mensagem = "abcdefghijklmnopqrstuvwxyz"
mensagem = mensagem.upper()
cifrada = ""
for letra in mensagem:
    # print(letra)
    # indice = alfabeto.index(letra)
    indice = ord(letra)
    #nova_letra = alfabeto[(indice + chave)%tamanho_alfabeto]
    novo_indice = (indice + chave)%tamanho_alfabeto
    if ( novo_indice > limite_alfabeto_minisculo or ( novo_indice > limite_alfabeto_maisculo and novo_indice < 97 )):
        novo_indice = novo_indice - letras_alfabeto

    nova_letra = chr( novo_indice )
    cifrada = cifrada + nova_letra

print(mensagem)
print(cifrada)