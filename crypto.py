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

chave = -3
mensagem = "AbcdefghijklmnopqrstuvwxyZ"
mensagem = mensagem.lower()
cifrada = ""
for letra in mensagem:
    #achar no alfabeto a letra que seja chave 
    indice = ord(letra)
    nova_letra = letra
    #fluxo maiúsculo
    if limite_inferior_maiusculo <= indice <= limite_superior_maiusculo:
        novo_indice = ( indice + chave)%(limite_superior_maiusculo+1) + ( (indice + chave)//(limite_superior_maiusculo+1) )*limite_inferior_maiusculo
        if indice + chave < limite_inferior_maiusculo:
            novo_indice = novo_indice + letras_alfabeto
        nova_letra = chr(novo_indice)
    #fluxo minusculas
    elif indice in range (limite_inferior_minisculo, limite_supeior_minisculo +1):
        novo_indice = (indice + chave)%(limite_supeior_minisculo+1) + ( (indice + chave)//(limite_supeior_minisculo+1))*limite_inferior_minisculo
        if indice + chave < limite_inferior_minisculo:
            novo_indice = novo_indice + letras_alfabeto
        nova_letra = chr(novo_indice)

 


    nova_letra = chr( novo_indice )
    cifrada = cifrada + nova_letra

print(mensagem)
print(cifrada)