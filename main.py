from Professor import Professor
from Aluno import Aluno
from Aula import Aula

if __name__ == '__main__':
    professor = Professor("Lucas")
    aluno1 = Aluno("Maria")
    aluno2 = Aluno("Pedro")
    aula = Aula(professor, "Programação Orientada a Objetos")
    aula.adicionar_alunos(aluno1)
    aula.adicionar_alunos(aluno2)
    print(aula.listar_presenca())
