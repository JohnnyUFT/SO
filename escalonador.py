# -*- coding: utf-8 -*-

'''
author: Johnny Pereira
email: johnnyuft@gmail.com
last modified: Dezembro 2017
'''

from random import randint
import arquivo
#from arquivo import *
import processo as p
#from processo import *
import matplotlib.pyplot as plt
import seaborn as sns


def sorteioIO(total_processos):
    """
    Sorteia qual, dentre os processos
     que estao na memoria, deverá ser bloqueado por IO.
    @param: total_processos: quantidade de processos na memória principal (executando)
    @return: 
    """
    sorteado = randint(0,total_processos)
    print(sorteado)

def sai_do_Bloqueio(fila_executando):
    """
    Escolhe um processo a ser desbloqueado,
    i.e, retira um processo da fila de bloqueio.
    :param fila_executando: fila de processos executando
    :return: processo que vai para fila de prontos
    """
    qtd = len(fila_executando)
    sorteado = randint(0,qtd)

    print(sorteado)
    return sorteado



# ********************************** #
# IMPLEMENTA UM ESCALONADOR de processos
# com filas dinâmicas...
# ********************************** #

class principal():
    """
    Classe principal deste projeto:
    Implementa o escalanonador, utilizando-se do módulo arquivo e
    da classe processo.
    """

    # lê dados .csv com arquivo.py:
    mat = arquivo.leArquivo()
    tam1 = len(mat[:][:]) # pega qtd de linhas da matriz

    ram = 20 # tamanho em 'KB' da memória ram (20k)

    fila = [] # pilha de processos recem criados
    for i in range(tam1):
        linha = mat[i][:]

        # instancia novo processo com atributos lidos:
        p1 = p.processo(linha[0], linha[1], linha[2], linha[3], linha[4])
        fila.append(p1)
        #print("i == %s"%i)

    # cria as 4 filas de prioridades:
    f0 = [] # prioridade 0
    f1 = [] # prioridade 1
    f2 = [] # prioridade 2
    f3 = [] # prioridade 3

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
    # Falta considerar a forma como se dará a tramitação entre as filas e a
    #  memória RAM, com processador, inclusive;
    #**************************************
    p1 = f0.pop()
    print(p1.getNome())

    # necessário qtd de processos na memória
    qtd_processos = 10 # só um exemplo
    

    sorteioIO(qtd_processos)

    sai_do_Bloqueio(f0) # f0, como exemplo

principal()