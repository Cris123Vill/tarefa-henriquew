# Programa para filtrar produtos por preço

produtos = [
    {"nome": "Notebook", "preco": 1500.00},
    {"nome": "Mouse", "preco": 35.00},
    {"nome": "Teclado", "preco": 120.00}
]

print("Produtos que custam mais de R$ 50,00:")
print("-" * 40)

for produto in produtos:
    if produto["preco"] > 50:
        print(f"- {produto['nome']}")