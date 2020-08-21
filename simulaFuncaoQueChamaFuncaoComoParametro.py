# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:46:04 2020

@author: Luciana
"""

#Sem a sintaxe da pizza @ do decorator

def programar():
    return 'Tome seu café antes de começar a programar!'

def tomar_cafe(func):
    print('Faça isso antes de executar programar()')
    print(func())
    
tomar_cafe(programar)
