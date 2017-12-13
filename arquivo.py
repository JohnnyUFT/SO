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
    df = pd.read_csv("dados.csv")
    #print(df1.head())

    mat = np.array(df, dtype=str)

    return mat
