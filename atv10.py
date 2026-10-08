# Programa de gerenciamento de notas de alunos

boletim = {}

# Laço while para adicionar alunos
while True:
    resposta = input("Deseja adicionar um aluno? (s/n): ").lower()
    
    if resposta == "s":
        nome = input("Digite o nome do aluno: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        
        boletim[nome] = nota
        print(f"✓ {nome} adicionado(a) com sucesso!\n")
    
    elif resposta == "n":
        print("\nFinalizando cadastro...\n")
        break
    
    else:
        print("Opção inválida! Digite 's' para sim ou 'n' para não.\n")

# Laço for para verificar aprovação/reprovação
if boletim:
    print("=" * 50)
    print("BOLETIM FINAL")
    print("=" * 50)
    
    for aluno, nota in boletim.items():
        if nota >= 6.0:
            status = "✓ Aprovado"
        else:
            status = "✗ Reprovado"
        
        print(f"{aluno}: {nota:.2f} - {status}")
    
    print("=" * 50)
else:
    print("Nenhum aluno foi cadastrado.")