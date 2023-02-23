from Professor import Professor
from Aluno import Aluno


class Aula:
    def __init__(self, prof, assunto):
        self.prof = prof
        self.assunto = assunto
        self.alunos = []

    def adicionar_alunos(self, Aluno):
        self.alunos.append(Aluno)

    def listar_presenca(self):
        for aluno_presente in self.alunos:
            aluno_presente.presenca()
