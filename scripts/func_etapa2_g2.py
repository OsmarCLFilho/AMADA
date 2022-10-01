import pandas as pd


def concatenar_elementos_coluna(DataFrame, coluna: str, condicao = None):
    dicionario = {}
    if condicao == None:
        indice = 'Todas'
        dicionario['Todas'] = ""
        anterior = None
        for line in range(len(DataFrame)):
            dado = DataFrame.loc[line, coluna]
            if dado == anterior:
                continue
            else:
                dicionario[indice] = dicionario[indice] + " " + dado
            anterior = dado
    else:
        for line in range(len(DataFrame)):
            indice = DataFrame.loc[line, condicao]
            dado = DataFrame.loc[line, coluna]
            if dicionario.get(indice):
                dicionario[indice] = dicionario[indice] + " " + dado
            else:
                dicionario[indice] = dado
    
    return dicionario


def concatenar_letras_album(DataFrame):
    dicionario = {}
    for line in range(len(DataFrame)):
        indice = DataFrame.loc[line, 'album']
        dado = DataFrame.loc[line, 'lyrics']
        if dicionario.get(indice):
            dicionario[indice] = dicionario[indice] + " " + dado
        else:
            dicionario[indice] = dado


def remove_contracoes(string: str):
    #contrações comuns no inglês
    chars = ["'m","'s","'re","n't","'ll","'ve","'d"]

    #faz um loop com as contrações para retirar suas ocorrências
    for str in chars:
        string = string.replace(str, "")

    #devido a contração de "cannot" ser "can't" e não "cann't", ao retirar as contrações, "can't" ficará "ca"
    string = string.replace(' ca ', " can ")

    return string


def remove_caracteres(string: str):
    #caracteres especiais que aparecem nos álbuns, nomes e letras das músicas
    chars = ["(",")","?","!","[","]",",",".","/","&","\"","'","-",":",";","“","”","‘","’","–","—"]

    #faz um loop com os caracteres para retirar suas ocorrências
    for str in chars:
        string = string.replace(str, "")

    return string


def remove_irrelevantes(string: str):
    with open("stopwords.txt") as file:
        stopwords = file.read().split()

    list_string = string.split()
    list_aux = list_string.copy()

    for str in list_aux:
        if str in stopwords:
            list_string.remove(str) 
    
    return list_string


def freq_elementos(list_string: list):
    indice = list_string.unique()

    dados = []

    for ind in indice:
        dados.append(list_string.count(ind))

    serie = pd.Series(data=dados, index=indice)
    serie = serie.sort_values(ascending=False)

    return serie