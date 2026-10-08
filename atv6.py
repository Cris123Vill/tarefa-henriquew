# Programa para calcular a média geral de notas

notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}

soma = 0

for aluno, nota in notas.items():
    soma += nota

media = soma / len(notas)

print("Notas dos alunos:")
for aluno, nota in notas.items():
    print(f"{aluno}: {nota}")

print(f"\nSoma total: {soma}")
print(f"Quantidade de alunos: {len(notas)}")
print(f"Média geral da turma: {media:.2f}")