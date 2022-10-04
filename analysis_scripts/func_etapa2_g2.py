import pandas as pd
import copy


def concat_elements_column(df: pd.DataFrame, coluna: str, key: str = None) -> dict:
    dictionary = {}
    if key == None:
        index = 'all'
        dictionary['all'] = ""
        anterior = None
        for line in range(len(df)):
            data = df.loc[line, coluna].upper()
            #se o data for igual ao adicionado anteriormente, ele não será colocado
            if data == anterior:
                continue
            else:
                dictionary[index] = dictionary[index] + " " + data
            anterior = data
    else:
        anterior = None
        for line in range(len(df)):
            index = df.loc[line, key]
            data = df.loc[line, coluna].upper()
            #se o data for igual ao adicionado anteriormente, ele não será colocado
            if data == anterior:
                continue
            else: 
                #se já houver o index, apenas soma o novo data ao anterior   
                if dictionary.get(index):
                    dictionary[index] = dictionary[index] + " " + data
                else:
                    #senão, cria um novo index com o data
                    dictionary[index] = data

    #faz a limpeza dos datas, referente a quebra de linha e informações entre os colchetes
    for key in dictionary.keys():
        dictionary[key] = dictionary[key].replace('\r\n', ' ').replace('_IGNORE_EMPTY_IGNORE_', ' ')
        depth = 0
        new_string = ""
        #retira os datas que estão entre colchetes e os colchetes
        for c in dictionary[key]:
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            elif depth == 0:
                new_string += c
        #se não houver nenhuma informação após retirar os dados desnecessários, guarda um aviso                
        if new_string.replace(' ', '') == '':
            dictionary[key] = '[Não possui nenhuma informação]'
        else:
            dictionary[key] = new_string
            
    return dictionary


def remove_contractions(dictionary: dict) -> dict:
    #contrações comuns no inglês
    chars = ["'M","'S","'RE","N'T","'LL","'VE","'D","’M","’S","’RE","N’T","’LL","’VE","’D"]

    #faz um loop com as contrações para retirar suas ocorrências
    for key in dictionary.keys():    
        if dictionary[key] == '[Não possui nenhuma informação]':
            continue
        else:    
            for string in chars:
                dictionary[key] = dictionary[key].replace(string, '')
            #devido a contração de "cannot" ser "can't" e não "cann't", ao retirar as contrações, "can't" ficará "ca"
            dictionary[key] = dictionary[key].replace(' ca ', ' can ')

    return dictionary


def remove_characters(dictionary: dict) -> dict:
    #caracteres especiais que aparecem nos álbuns, nomes e letras das músicas
    chars = ["(",")","?","!","[","]",",",".","/","&","\"","'","-",":",";","“","”","‘","’","–","—"]

    for key in dictionary.keys():    
        if dictionary[key] == '[Não possui nenhuma informação]':
            continue
        else: 
            #faz um loop com os caracteres para retirar suas ocorrências
            for string in chars:
                dictionary[key] = dictionary[key].replace(string, "")

    return dictionary


def remove_undesirables(dictionary: dict) -> dict:
    with open("stopwords.txt") as file:
        #transforma o arquivo de texto em uma lista e põe todas as palavras em letras maiúsculas
        stopwords = file.read().upper().split()
    
    for key in dictionary.keys():
        if dictionary[key] == '[Não possui nenhuma informação]':
            continue
        else:
            #transforma os valores do dictionary em listas
            dictionary[key] = dictionary[key].split()
 
    dictionary_aux = copy.deepcopy(dictionary)

    for key in dictionary.keys():    
        if dictionary[key] == '[Não possui nenhuma informação]':
            continue
        else: 
            #retira as palavras que estão na lista stopword 
            for string in dictionary_aux[key]:
                if string in stopwords:
                    dictionary[key].remove(string) 
    
    return dictionary


def elements_freq(dictionary: dict) -> dict:
    for key in dictionary.keys():  
        if dictionary[key] == '[Não possui nenhuma informação]':
            continue
        else: 
            #se caso receber um dicionário em que os valores são strings, irá transformá-los em listas
            if not isinstance(dictionary[key], list):
                dictionary[key] = dictionary[key].split()
            #define a lista de índices como as palavras que cada valor do dictionary possui
            index = list(set(dictionary[key]))
            datas = []

            for ind in index:
                #adiciona quantas vezes cada palavra aparece no valor do dictionary na ordem da lista índice
                datas.append(dictionary[key].count(ind))

            #cria a série com os índices e os datas, e coloca ela em ordem decrecescente
            serie = pd.Series(data=datas, index=index, dtype='int64')
            serie = serie.sort_values(ascending=False)

            dictionary[key] = serie

    return dictionary


def relevancy(dictionary: dict) -> dict:
    for key in dictionary.keys():
        if dictionary[key] == '[Não possui nenhuma informação]':
            continue
        else:
            #coloca em cada valor do dicionário a quantidade que o key repete no valor anterior
            dictionary[key] = dictionary[key].count(key)
    
    return dictionary
