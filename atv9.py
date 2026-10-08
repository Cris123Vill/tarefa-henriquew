# Programa para extrair vogais de uma palavra

palavra = input("Digite uma palavra: ")
vogais = []

for letra in palavra:
    if letra.lower() in "aeiou":
        vogais.append(letra)

print(f"\nPalavra digitada: {palavra}")
print(f"Vogais encontradas: {vogais}")
print(f"Quantidade de vogais: {len(vogais)}")