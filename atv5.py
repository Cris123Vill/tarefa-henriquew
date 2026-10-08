# Programa para armazenar dados do usuário em um dicionário

dados = {}

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
email = input("Digite seu e-mail: ")

dados["nome"] = nome
dados["telefone"] = telefone
dados["email"] = email

print("\n--- Dados Armazenados ---")
print(dados)