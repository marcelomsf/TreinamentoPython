# Quantos anos você tem?
# idade
# Se idade < 16 então :
# - Você não pode votar
idade = int( input ("Quantos anos você tem ?\n") )
if ( idade < 16 ):
    print("Você não pode votar!" )
elif ( idade < 18  or idade > 70 ):
    print("Você pode votar!")
elif ( idade < 70 ):
    print("Você deve votar")


print ("FIM")    
