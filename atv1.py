# Programa para verificar se um número é par ou ímpar

numero = int(input("digite um numero inteiro:"))

if numero == 0:
    print("o numero é neutro")

elif numero % 2 == 0:
    print(f"o numero{numero} é par")
    
else:
    print (f"o numero {numero} é ímpar")