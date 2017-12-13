# -*- coding: utf-8 -*-

'''
author: Johnny Pereira
email: johnnyuft@gmail.com
last modified: Novembro 2017
'''

import threading
import time
import arquivo
#from arquivo import *
import processo as p
#from processo import *
import matplotlib.pyplot as plt
import seaborn as sns

# ********************************** #
# IMPLEMENTA UM ESCALONADOR de processos
# com filas dinâmicas...
# ********************************** #

class main():
    """
    Classe principal deste projeto:
    Implementa o escalanonador, utilizando-se do módulo arquivo e
    da classe processo.
    """

    # lê dados .csv com arquivo.py:
    mat = arquivo.leArquivo()
    tam1 = len(mat[:][:]) # pega qtd de linhas da matriz

    ram = 20

    fila = [] # pilha de processos recem criados
    for i in range(tam1):
        linha = mat[i][:]

        # instancia novo processo com atributos lidos:
        p1 = p.processo(linha[0], linha[1], linha[2], linha[3], linha[4])
        fila.append(p1)
        #print("i == %s"%i)

    # cria as 4 filas de prioridades:
    f0 = [] #
    f1 = []
    f2 = []
    f3 = []

    # separa os processos entre as filas de prioridades:
    for p in range(len(fila)):
        p2 = fila.pop()
        prioridade = p2.getPrioridade()

        if(prioridade == 0):
            f0.append(p2)
        elif(prioridade == 1):
            f1.append(p2)
        elif(prioridade == 2):
            f2.append(p2)
        else:
            f3.append(p2)

    #**************************************
    # Ate aqui, pega os processos e separa-os conforme as filas de prioridades
    # Falta reconsidrerar as condições para este fato;
    # Falta considerar a forma como se dará a tramitação entre as filas e a
    #  memória RAM, com processador, inclusive;
    #**************************************
    p1 = f0.pop()
    print(p1.getNome())


main()