#!/usr/bin/python3
import sys
import os.path
from banco import Arquivo
from sqlitemodel import SQL

def ajuda(appname):
    print("Use:\t\t" + appname + " <arquivo_txt>")
    print("Onde:\t\t<arquivo_txt> - nome do arquivo a ser analisado.\n")
    print("Obs.:\t\taltera o arquivo '/home/msilva/proj/analfiles/database.db'\n")
    print("Formato:\tfile=\"path_do_arquivo\" md5sum=\"md5sum_do_arquivo\" data=\"data_do_arquivo\" size=\"tamanho_do_arquivo\"")

def ArquivoExiste(arquivo):
    arquivo = Arquivo().selectOne(SQL().WHERE('arquivo','=',arquivo))
    return arquivo != None

if __name__ == "__main__":

    print(sys.argv[0] + ' - SOB Software - 2020 copyright\n')

    if len(sys.argv) != 2:
        ajuda(sys.argv[0])
        quit()
    else:
        nome=sys.argv[1]

    filesize, ultimo, atual, total = os.path.getsize(nome),-1, 0, 0

    infile = open(nome, "r")

    for linha in infile:    
        
        campos = linha.split('"')

        if not ArquivoExiste(campos[1]):
            arquivo = Arquivo()
            arquivo.createTable()
            arquivo.arquivo = campos[1]
            arquivo.md5sum = campos[3]
            arquivo.data = campos[5]
            arquivo.tamanho = campos[7]
            arquivo.save()
            total+=1
        '''else:
            print(campos[1], ' já existe!')'''

        atual += len(linha)
        estado = int(atual/filesize * 100)

        if (ultimo != estado):
            print('\restado: {0}'.format(estado), end='')
            ultimo = estado

    infile.close()

    print('\n')
    print(str(total) + ' registros inseridos!')
