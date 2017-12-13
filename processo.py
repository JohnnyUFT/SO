# CLASSE processo com todos seus atributos e métodos:

class processo:
    """
    Classe processo com seus atributos e métodos característicos:
    """
    def __init__(self, pid, nome, espaco_memoria, tempo_cpu, prioridade):
        # Recursos Alocados:
        self.nome = nome
        self.pid = pid # identificados do processo
        self.prioridade = prioridade
        self.tempo_cpu = tempo_cpu
        # Enderecos de memoria:
        self.status = 0
        self.espaco_memoria = espaco_memoria

    # getters:
    def getNome(self):
        return str(self.nome)
    def getPid(self):
        return int(self.pid)
    def getPrioridade(self):
        return int(self.prioridade)
    def getTempo(self):
        return int(self.tempo_cpu)
    def getStatus(self):
        return int(self.status)
    def getEspacoMemoria(self):
        return float(self.espaco_memoria)

    #setters:
    def setNome(self, nome):
        #pass # nome nao muda
        self.nome = nome
    def setPid(self, pid):
        #pass # pid nao muda
        self.pid = pid
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