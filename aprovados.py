aprovados = [
    "Graziela Barroso", "Juliano Moreira", "André Rebouças", "César Lattes","Enedina Alves",
    "Machado de Assis", "Ayrton Senna", "Luiz Gamma", "Ruth de Souza", "Nise da Silveira",
    "Johanna Döbereiner", "Carolina de Jesus", "Leopoldo Nachbin", "Antonieta de Barros", "Lima Barreto"
    ]

vagas = int(input("Digite o número de vagas: "))

print("A lista: ", aprovados)
print ("A primeira colocado: ", aprovados[0])

# 1. Quantidade total de aprovados
print("Total de aprovados: ", len(aprovados))
# 2. Primeira pessoa na condição de reserva
print("Primeiro reserva: ",aprovados[vagas])
# 3. Verificar se alguém está na lista
if "Oswaldo Cruz" in aprovados:
    print("Parabéns, Oswaldo")
else:
    print("Uma pena, não foi dessa vez")
# 4. Listar de classificados
classificados = aprovados[0:vagas]
print("Classificados: ",classificados)
# 5. Lista de reservas
reservas = aprovados[vagas:len(aprovados)]
print("Reservas: ",reservas)
# 6. Último Classificado
print("Último classificado: ", classificados[-1])
# 7.Último Reserva
print("Último reserva: ", reservas[-1])