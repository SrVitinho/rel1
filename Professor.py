class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministraraulas(self):
        assuntos = input("Assunto da aula: ")
        print("O Professor " + self.nome + " está ministrando uma aula sobre " + assuntos)
