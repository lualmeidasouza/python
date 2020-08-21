# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:11:46 2020

@author: Luciana
"""

def meu_decorador(func):
    def empacotador():
        print('Antes da chamada da função')
        func()
        print('Depois da chamada da função')
    return empacotador

@meu_decorador
def diga_onde():
    print('diga_onde() function')
    
    #estas três linhas acima, nada 

diga_onde()
