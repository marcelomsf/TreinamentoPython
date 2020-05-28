def substituir(indice, chave, limite_inferior, limite_superior):
    letras_alfabeto = limite_superior - limite_inferior + 1
    novo_indice = ( indice + chave)%(limite_superior+1) + ( (indice + chave)//(limite_superior+1) )*limite_inferior
    if indice + chave < limite_inferior:
        novo_indice = novo_indice + letras_alfabeto
    return chr(novo_indice)

def criptografar (mensagem, chave):

    #Limetes em relacao a tabela ASCII
    limite_supeior_minisculo=ord('z')
    limite_inferior_minisculo=ord('a')
    limite_superior_maiusculo= ord('Z')
    limite_inferior_maiusculo = ord('A')


    cifrada = ""
    for letra in mensagem:
        #achar no alfabeto a letra que seja chave 
        indice = ord(letra)
        nova_letra = letra
        #fluxo maiúsculo
        if limite_inferior_maiusculo <= indice <= limite_superior_maiusculo:
            nova_letra = substituir(indice, chave, limite_inferior_maiusculo, limite_superior_maiusculo)
        #fluxo minusculas
        elif indice in range (limite_inferior_minisculo, limite_supeior_minisculo +1):
            nova_letra = substituir(indice, chave, limite_inferior_minisculo, limite_supeior_minisculo)
        
        cifrada = cifrada + nova_letra

    return cifrada

def descriptografar(mensagem, chave):
    return criptografar(mensagem, -chave)


chave = int(input("Digite um número interiro: "))
mensagem = input("Digite a mensagem a ser criptografada: ")

crifrada = criptografar (mensagem, chave)
print(crifrada)
decrifrada = descriptografar(crifrada, chave)
print(decrifrada)