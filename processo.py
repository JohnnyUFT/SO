# CLASSE processo com todos seus atributos e métodos:

class processo:
    def __init__(self):
        # Recursos Alocados:
        self.nome = nome
        self.pid = pid # identificados do processo
        self.prioridade = prioridade
        self.tempo_cpu = tempo_cpu

        # Enderecos de memoria:
        self.status = status # inteiro
        self.espaco_memoria = espaco_memoria # tupla

    # getters:
    def getNome(self):
        return self.nome
    def getPid(self):
        return self.pid
    def getPrioridade(self):
        retun self.prioridade
    def getTempo(self):
        return self.tempo_cpu
    def getStatus(self):
        return self.status
    def getEspacoMemoria(self):
        return self.espaco_memoria

    setters:
    def setNome(self):
        pass # nome nao muda
    def setPid(self):
        pass # pid nao muda
    def setPrioridade(self, prioridade):
        self.prioridade = prioridade
    def setTempo(self):
        pass # nao muda
    def setStatus(self, status):
        self.status = status
    def setEspacoMemoria(self):
        pass # nao sei se muda

    # metodos adicionais:
    def facaAlgo(self):
        pass
