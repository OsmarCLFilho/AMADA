import pandas as pd
import copy


def concatenar_elementos_coluna(DataFrame: pd.DataFrame, coluna: str, condicao: str = None) -> dict:
    dicionario = {}
    if condicao == None:
        indice = 'Todas'
        dicionario['Todas'] = ""
        anterior = None
        for line in range(len(DataFrame)):
            dado = DataFrame.loc[line, coluna].upper()
            #se o dado for igual ao adicionado anteriormente, ele não será colocado
            if dado == anterior:
                continue
            else:
                dicionario[indice] = dicionario[indice] + " " + dado
            anterior = dado
    else:
        anterior = None
        for line in range(len(DataFrame)):
            indice = DataFrame.loc[line, condicao]
            dado = DataFrame.loc[line, coluna].upper()
            #se o dado for igual ao adicionado anteriormente, ele não será colocado
            if dado == anterior:
                continue
            else: 
                #se já houver o indice, apenas soma o novo dado ao anterior   
                if dicionario.get(indice):
                    dicionario[indice] = dicionario[indice] + " " + dado
                else:
                    #senão, cria um novo indice com o dado
                    dicionario[indice] = dado

    #faz a limpeza dos dados, referente a quebra de linha e informações entre os colchetes
    for key in dicionario.keys():
        dicionario[key] = dicionario[key].replace('\r\n', ' ').replace('_IGNORE_EMPTY_IGNORE_', ' ')
        profundidade = 0
        novo_texto = ""
        #retira os dados que estão entre colchetes e os colchetes
        for c in dicionario[key]:
            if c == "[":
                profundidade += 1
            elif c == "]":
                profundidade -= 1
            elif profundidade == 0:
                novo_texto += c
        
        dicionario[key] = novo_texto
            
    return dicionario


def remove_contracoes(dicionario: dict) -> dict:
    #contrações comuns no inglês
    chars = ["'M","'S","'RE","N'T","'LL","'VE","'D","’M","’S","’RE","N’T","’LL","’VE","’D"]

    #faz um loop com as contrações para retirar suas ocorrências
    for key in dicionario.keys():    
        for str in chars:
            dicionario[key] = dicionario[key].replace(str, "")
        #devido a contração de "cannot" ser "can't" e não "cann't", ao retirar as contrações, "can't" ficará "ca"
        dicionario[key] = dicionario[key].replace(' ca ', " can ")

    return dicionario


def remove_caracteres(dicionario: dict) -> dict:
    #caracteres especiais que aparecem nos álbuns, nomes e letras das músicas
    chars = ["(",")","?","!","[","]",",",".","/","&","\"","'","-",":",";","“","”","‘","’","–","—"]

    for key in dicionario.keys():    
        #faz um loop com os caracteres para retirar suas ocorrências
        for str in chars:
            dicionario[key] = dicionario[key].replace(str, "")

    return dicionario


def remove_irrelevantes(dicionario: dict) -> dict:
    with open("stopwords.txt") as file:
        #transforma o arquivo de texto em uma lista e põe todas as palavras em letras maiúsculas
        stopwords = file.read().upper().split()
    
    for key in dicionario.keys():
        #transforma os valores do dicionario em listas
        dicionario[key] = dicionario[key].split()
 
    dicionario_aux = copy.deepcopy(dicionario)

    for key in dicionario.keys():    
        #retira as palavras que estão na lista stopword 
        for str in dicionario_aux[key]:
            if str in stopwords:
                dicionario[key].remove(str) 
    
    return dicionario


def freq_elementos(dicionario: dict) -> dict:
    for key in dicionario.keys():  
        #define a lista de índices como as palavras que cada valor do dicionario possui
        indice = list(set(dicionario[key]))
        dados = []

        for ind in indice:
            #adiciona quantas vezes cada palavra aparece no valor do dicionario na ordem da lista índice
            dados.append(dicionario[key].count(ind))

        #cria a série com os índices e os dados, e coloca ela em ordem decrecescente
        serie = pd.Series(data=dados, index=indice, dtype='int64')
        serie = serie.sort_values(ascending=False)

        dicionario[key] = serie

    return dicionario


def relevancia(dicionario: dict) -> dict:
    for key in dicionario.keys():
        #coloca em cada valor do dicionário a quantidade que o key repete no valor anterior
        dicionario[key] = dicionario[key].count(key)
    
    return dicionario
