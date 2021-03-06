import csv
from Docentes import Docentes
from Veiculos import Veiculos
from Publicacoes import Publicacoes
from Regras import Regras

from datetime import datetime
from functools import reduce

def main():
    listaDocentes = ler_arquivo_docentes()
    listaVeiculos = ler_arquivo_veiculos()
    listaPublicacoes = ler_arquivo_publicacoes(listaVeiculos, listaDocentes)
    ler_arquivo_qualis(listaVeiculos)
    regras = ler_arquivo_regras()


    print("DOCENTES")

    for i in listaDocentes:
        print(i)
    
    print("VEICULOS")

    for i in listaVeiculos:
        print(i)

    print("PUBLICACOES")
    for i in listaPublicacoes:
        print(i)
        
    print("REGRAS")
    
    print(regras)

    write_lista_publicacoes()


def ler_arquivo_docentes():
    path = 'docentes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaDocentes = []
    for row in reader:
        codigo = str(row[0])
        nome = str(row[1])
        data_nascimento = datetime.strptime(row[2], '%d/%m/%Y')
        data_ingresso = datetime.strptime(row[3], '%d/%m/%Y')
        coordenador = str(row[4]) == 'X'

        docente = Docentes(nome, codigo, data_nascimento, data_ingresso, coordenador)
        listaDocentes.append(docente)

    return listaDocentes

def ler_arquivo_veiculos():
    path = 'veiculos.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaVeiculos = []
    for row in reader:
        sigla = str(row[0])
        nome = str(row[1])
        tipo = str(row[2])
        fator = float(str(row[3]).replace(',','.'))
        issn = str(row[4])

        veiculo = Veiculos(sigla, nome, tipo, fator, issn)
        listaVeiculos.append(veiculo)

    return listaVeiculos

def ler_arquivo_publicacoes(listaVeiculos, listaDocentes):
    path = 'publicacoes.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    listaPublicacoes =[]

    for row in reader:
        ano = datetime.strptime(row[0], '%Y')
        for i in listaVeiculos:
            if i.sigla == str(row[1]):
                veiculo = i

        titulo = str(row[2])
        listaAutores = []
        codigos = []
        codigos = str(row[3]).split(",")
        for i in listaDocentes:
            if i.codigo in codigos:
                listaAutores.append(i)
                
        numero = int(row[4])
        volume = str(row[5])
        local = str(row[6])
        pagina_inicial = int(row[7])
        pagina_final = int(row[8])

        publicacao = Publicacoes(ano, veiculo, titulo, listaAutores, numero, volume, local, pagina_inicial, pagina_final)
        listaPublicacoes.append(publicacao)
    return listaPublicacoes

def ler_arquivo_qualis(listaVeiculos):
    path = 'qualis.csv'
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha

    for row in reader:
        ano = int(str(row[0]))
        qualis = str(row[2])
        for i in listaVeiculos:
            if i.sigla == str(row[1]):
                i.anoSet(ano)
                i.qualisSet(qualis)
                #print(ano, qualis, i)
        
def ler_arquivo_regras(): 
    path ='regras.csv'   
    file = open(path, newline='', encoding="utf8")
    reader = csv.reader(file, delimiter = ';')

    header = next(reader) # Primeira linha
    for row in reader:
        data_inicio = datetime.strptime(row[0], '%d/%m/%Y')
        data_fim = datetime.strptime(row[1], '%d/%m/%Y')
        qualis = row[2].split(',')
        score = row[3].split(',')
        ponto_regra  = dict(zip(qualis,score))
        #print(ponto_regra)
        multiplicador = row[4]
        anos_considerar = row[5]
        minimo_pontos = row[6]

        #print( multiplicador,anos_considerar,minimo_pontos)
    regras = Regras(multiplicador,data_inicio,data_fim,anos_considerar,minimo_pontos,ponto_regra)
    return regras

def write_lista_publicacoes():
    print('this is from the lista de publicacoes function !!!')


main()


