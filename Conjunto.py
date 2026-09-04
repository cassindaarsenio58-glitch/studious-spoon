alunos_turma_a = {"Ana", "Bruno", "Carla", "Daniel"}
alunos_turma_b = {"Carla", "Daniel", "Eduardo", "Fernanda"}

alunos_turma_a.add("Gabriel")

print("Alunos na Turma A:", alunos_turma_a)

alunos_em_ambas = alunos_turma_a.intersection(alunos_turma_b)
print("Alunos matriculados em ambas as turmas:", alunos_em_ambas)

todos_alunos = alunos_turma_a.union(alunos_turma_b)
print("Total de alunos únicos na escola:", todos_alunos)
