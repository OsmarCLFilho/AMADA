import func_etapa2_g2 as fe
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys

try:
    df = pd.read_csv("../results/spo_lyr_data.csv")

except FileNotFoundError:
    print("spo_lyr_data.csv not found in /results/. The file structure of the project is altered!")
    sys.exit(1)

############################################################################################################

dictionary = fe.concat_elements_column(df, 'album')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)

string = dictionary['all']

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("visualizacao_e2_g2_out/questao1.png")

############################################################################################################

dictionary = fe.concat_elements_column(df, 'name')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)

string = dictionary['all']

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("visualizacao_e2_g2_out/questao2.png")

############################################################################################################

dictionary = fe.concat_elements_column(df, 'lyrics')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)
dictionary = fe.remove_undesirables(dictionary)
string = " ".join(dictionary['all'])

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("visualizacao_e2_g2_out/questao4.png")
