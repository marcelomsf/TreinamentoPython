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
#Limetes em relacao a tabela ASCII
limite_supeior_minisculo=ord('z')
limite_inferior_minisculo=ord('a')
limite_superior_maiusculo= ord('Z')
limite_inferior_maiusculo = ord('A')
letras_alfabeto = limite_supeior_minisculo - limite_inferior_minisculo + 1

chave = 3
mensagem = "AbcdefghijklmnopqrstuvwxyZ"
mensagem = mensagem.upper()
cifrada = ""
for letra in mensagem:
    # print(letra)
    # indice = alfabeto.index(letra)
    indice = ord(letra)
    #nova_letra = alfabeto[(indice + chave)%tamanho_alfabeto]
    novo_indice = (indice + chave)%tamanho_alfabeto
    if (( novo_indice > limite_supeior_minisculo )or ( novo_indice > limite_superior_maiusculo and novo_indice < limite_inferior_minisculo)):
        novo_indice = novo_indice - letras_alfabeto
    

    nova_letra = chr( novo_indice )
    cifrada = cifrada + nova_letra

print(mensagem)
print(cifrada)