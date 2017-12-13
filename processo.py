# CLASSE processo com todos seus atributos e métodos:

class processo:
    """
    Classe processo com seus atributos e métodos característicos:
    """
    def __init__(self, pid, nome, espaco_memoria, quantum, prioridade):
        # Recursos Alocados:
        self.nome = nome
        self.pid = pid # identificador do processo
        self.prioridade = prioridade # identifica a fila de prioridade em que está
        self.quantum = quantum # quantos tempo de CPU precisa
        self.status = 0 # se pronto, bloqueado, executando
        self.espaco_memoria = espaco_memoria # quanto gasta da memória principal

    # getters:
    def getNome(self):
        return str(self.nome)
    def getPid(self):
        return int(self.pid)
    def getPrioridade(self):
        return int(self.prioridade)
    def getTempo(self):
        return int(self.quantum)
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

    # diz quanto de tempo ainda precisa para rodar na CPU:
    def setTempo(self, quantumRestante):
        self.quantum = quantumRestante
    
    def setStatus(self, status):
        self.status = status
    def setEspacoMemoria(self):
        pass # nao muda

    # metodos adicionais:
    def facaAlgo(self):
        pass # desnecessários