class Mes:

    def __init__(self, nome, dias_letivos):

        self.nome = nome
        self.dias_letivos = dias_letivos * 9
        self.passou = True
        self.frequencia = 100
        self.faltas = 0

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getDias(self):
        return self.dias_letivos

    def setDias(self, dias):
        self.dias_letivos = dias

    def getPassou(self):
        return self.passou

    def setPassou(self, passou):
        self.passou = passou

    def getFrequencia(self):
        return self.frequencia

    def setFrequencia(self, frequencia):
        self.frequencia = frequencia

    def getFaltas(self):
        return self.faltas

    def setFaltas(self, faltas):
        self.faltas = faltas

    def porcentagem(self):
        self.frequencia = (100*(self.dias_letivos - self.faltas)) // self.dias_letivos
        return self.frequencia
