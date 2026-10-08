# Programa para imprimir a tabuada de um número

numero = int(input("Digite um número de 1 a 10: "))

print(f"\nTabuada do {numero}:")
print("-" * 20)

if numero < 1 or numero >10:
 print(f"se o numero for maior que 10 ou menor que 1 o codigo não será executado")
 
else:
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")