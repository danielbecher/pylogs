# -*- coding: utf-8 -*-
#Processamento de logs do DOMLOGS do Apache cPanel/WHM para o fail2ban
#Importa as bibliotecas necessárias
import re
import time
from pathlib import Path
import os

#seta os diretórios
dirlogs = "logs/"
dirout = "fail2ban/"
listaArquivos = []
_start_time = time.time()
counter = 0

def lista_arquivos():
    global counter
    print('### Importando lista de arquivos para análise de XMLRPC')
    for path, currentDirectory, files in os.walk("logs/"):
        for file in files:
            listaArquivos.append(os.path.join(path, file))
    for cont in range(len(listaArquivos)):
        findXmlrpc(listaArquivos[cont])
    print('Foram encontrados {} registros!'.format(counter))
    
    print('### Importando lista de arquivos para análise de WP-LOGIN')
    for path, currentDirectory, files in os.walk("logs/"):
        for file in files:
            listaArquivos.append(os.path.join(path, file))
    for cont in range(len(listaArquivos)):
        findWplogin(listaArquivos[cont])
    print('Foram encontrados {} registros!'.format(counter))

def findXmlrpc(arquivo):
    global counter
    with open(arquivo, 'r') as a:
        for line in a:
            if re.findall('xmlrpc.php', line):
                counter += 1
                with open(dirout + 'xmlrpc.txt', 'a') as x:
                    x.write(line)
                    x.close()
    return counter

def findWplogin(arquivo):
    global counter
    with open(arquivo, 'r') as a:
        for line in a:
            if re.findall('wp-login.php', line):
                counter += 1
                with open(dirout + 'wp-login.txt', 'a') as x:
                    x.write(line)
                    x.close()
    return counter
    
def tic():
    global _start_time 
    _start_time = time.time()

def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec,60)
    (t_hour,t_min) = divmod(t_min,60) 
    print('Tempo total de processamento: {}hour:{}min:{}sec'.format(t_hour,t_min,t_sec))

tic()
lista_arquivos()
tac()