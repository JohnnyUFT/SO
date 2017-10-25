# -*- coding: utf-8 -*-

'''
author: Johnny Pereira
email: johnnyuft@gmail.com
last modified: Outubro 2017
'''

import numpy as np
import pandas as pd

def leArquivo():
    # lê o arquivo:
    fin = open('arquivo', 'rt' )
    while True:
        linha = fin.readline()
        if not linha:
            break
        trataLinhas(linha)
    fin.close()

# Define o que acontece com cada linha lida do arquivo;
def trataLinhas(linha):
    pass
