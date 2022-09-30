import pandas as pd

#with open("stopwords.txt") as file:
    #stopwords = file.read().replace('\n', ' ')

#stopwords = stopwords.split()
stopwords = ['you','your']

df = pd.read_csv('./../results/alb_lyrics.csv')

lista = df["lyrics"]
string = ""

#somando as linhas da coluna lyrics para ficar em uma só string todas as letras
for i in lista:
    string = string + " " + i

#caracteres que serão retirados para fazer uma limpeza
chars = ["'m","'s","'re","n't","'ll","'ve","'d","(",")","?","!","[","]",",",".","/","&","\"","'","-",":",";","“","”","‘","’","–","—"]

#retirada dos caracteres
for str in chars:
    string = string.replace(str, "")
