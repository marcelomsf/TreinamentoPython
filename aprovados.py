aprovados = [
    "Graziela Barroso", "Juliano Moreira", "André Rebouças", "César Lattes","Enedina Alves",
    "Machado de Assis", "Ayrton Senna", "Luiz Gamma", "Ruth de Souza", "Nise da Silveira",
    "Johanna Döbereiner", "Carolina de Jesus", "Leopoldo Nachbin", "Antonieta de Barros", "Lima Barreto"
    ]

print("A lista: ", aprovados)
print ("A primeira colocado: ", aprovados[0])

# 1. Quantidade total de aprovados
print("Total de aprovados: ", len(aprovados))
# 2. Primeira pessoa na condição de reserva
print("Primeiro reserva: ",aprovados[5])
# 3. Verificar se alguém está na lista
if "Oswaldo Cruz" in aprovados:
    print("Parabéns, Oswaldo")
else:
    print("Uma pena, não foi dessa vez")
# 4. Listar de classificados
classificados = aprovados[0:5]
print("Classificados: ",classificados)
# 5. Lista de reservas
reservas = aprovados[5:len(aprovados)]
print("Reservas: ",reservas)