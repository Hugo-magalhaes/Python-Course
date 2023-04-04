from itertools import groupby, tee

alunos = [
    {'nome': 'Hugo', 'nota': 'A'},
    {'nome': 'Bruna', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'José', 'nota': 'C'},
    {'nome': 'Amanda', 'nota': 'D'},
    {'nome': 'Rose', 'nota': 'D'},
    {'nome': 'Nathan', 'nota': 'D'},
    {'nome': 'Vinícius', 'nota': 'D'},
]

ordem = lambda item: item['nota']
alunos.sort(key=ordem)

aluno_agroup = groupby(alunos, ordem)

for notas, quantidade in aluno_agroup:
    va1, va2 = tee(quantidade) # Fez duas cópias do iterador
    print(f' Nota {notas} teve {len(list(va2))} alunos')
    for aluno in va1: 
        print(aluno)
