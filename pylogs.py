#Processamento de logs do DOMLOGS do Apache cPanel/WHM para o fail2ban

#Importa as bibliotecas necessárias
import re


#seta os diretórios
dirlogs = "logs/"
dirout = "fail2ban/"

arq = open('logs/liber_log', 'r')
texto = arq.readlines()
for line in texto:
    print(line)
arq.close()