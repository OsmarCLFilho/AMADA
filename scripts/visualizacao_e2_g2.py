import func_etapa2_g2 as fe
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


df = pd.read_csv("spo_lyr_data.csv")

############################################################################################################

dicionario = fe.concatenar_elementos_coluna(df, 'album')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)

string = dicionario['Todas']

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("questao1.png")

############################################################################################################

dicionario = fe.concatenar_elementos_coluna(df, 'name')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)

string = dicionario['Todas']

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("questao2.png")

############################################################################################################

dicionario = fe.concatenar_elementos_coluna(df, 'lyrics')
dicionario = fe.remove_contracoes(dicionario)
dicionario = fe.remove_caracteres(dicionario)
dicionario = fe.remove_irrelevantes(dicionario)
string = " ".join(dicionario['Todas'])

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("questao4.png")