import pandas as pd
import copy


def concatenar_elementos_coluna(DataFrame: pd.DataFrame, coluna: str, condicao: str = None):
    dicionario = {}
    if condicao == None:
        indice = 'Todas'
        dicionario['Todas'] = ""
        anterior = None
        for line in range(len(DataFrame)):
            dado = DataFrame.loc[line, coluna].upper()
            if dado == anterior:
                continue
            else:
                dicionario[indice] = dicionario[indice] + " " + dado
            anterior = dado
    else:
        for line in range(len(DataFrame)):
            indice = DataFrame.loc[line, condicao]
            dado = DataFrame.loc[line, coluna].upper()
            if dicionario.get(indice):
                dicionario[indice] = dicionario[indice] + " " + dado
            else:
                dicionario[indice] = dado
    for key in dicionario.keys():
        dicionario[key] = dicionario[key].replace('\r\n', ' ').replace('_IGNORE_EMPTY_IGNORE_', ' ')
        profundidade = 0
        novo_texto = ""
        for c in dicionario[key]:
            if c == "[":
                profundidade += 1
            elif c == "]":
                profundidade -= 1
            elif profundidade == 0:
                novo_texto += c
        
        dicionario[key] = novo_texto
            
    return dicionario


def remove_contracoes(dicionario: dict):
    #contrações comuns no inglês
    chars = ["'M","'S","'RE","N'T","'LL","'VE","'D"]

    #faz um loop com as contrações para retirar suas ocorrências
    for key in dicionario.keys():    
        for str in chars:
            dicionario[key] = dicionario[key].replace(str, "")
        #devido a contração de "cannot" ser "can't" e não "cann't", ao retirar as contrações, "can't" ficará "ca"
        dicionario[key] = dicionario[key].replace(' ca ', " can ")

    return dicionario


def remove_caracteres(dicionario: dict):
    #caracteres especiais que aparecem nos álbuns, nomes e letras das músicas
    chars = ["(",")","?","!","[","]",",",".","/","&","\"","'","-",":",";","“","”","‘","’","–","—"]

    #faz um loop com os caracteres para retirar suas ocorrências
    for key in dicionario.keys():    
        for str in chars:
            dicionario[key] = dicionario[key].replace(str, "")

    return dicionario


def remove_irrelevantes(dicionario: dict):
    with open("stopwords.txt") as file:
        stopwords = file.read().upper().split()
    
    for key in dicionario.keys():
        dicionario[key] = dicionario[key].split()
 
    dicionario_aux = copy.deepcopy(dicionario)

    for key in dicionario.keys():     
        for str in dicionario_aux[key]:
            if str in stopwords:
                dicionario[key].remove(str) 
    
    return dicionario


def freq_elementos(dicionario: dict):
    for key in dicionario.keys():    
        indice = list(set(dicionario[key]))
        dados = []

        for ind in indice:
            dados.append(dicionario[key].count(ind))

        serie = pd.Series(data=dados, index=indice, dtype='int64')
        serie = serie.sort_values(ascending=False)

        dicionario[key] = serie

    return dicionario


def relevancia(dicionario):
    for key in dicionario.keys():
        dicionario[key] = dicionario[key].count(key)
    
    return dicionario
