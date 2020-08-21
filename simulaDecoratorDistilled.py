# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:46:04 2020

@author: 89292693
"""

def meu_decorador(func):
    def empacotador():
        print('Antes de chamar a função "diga_onde()"')
        func() #Aqui ele chama a função que foi passada como parâmetro para a função principal
        print('Depois de chamaar a função...')
        return empacotador
    
def diga_onde():
    print('Esta é a função diga_onde()')
    
diga_onde = meu_decorador(diga_onde)

