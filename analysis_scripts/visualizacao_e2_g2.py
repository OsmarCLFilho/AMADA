import func_etapa2_g2 as fe
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys

try:
    df = pd.read_csv("../results/final_dataset.csv")

except FileNotFoundError:
    print("final_dataset.csv was not found in /results/. The file structure of the project is altered!")
    sys.exit(1)

############################################################################################################

######  QUESTION 1  ######

dictionary = fe.concat_elements_column(df, 'album')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)

string = dictionary['all']
freq = fe.elements_freq(dictionary)
dict_freq = freq["all"].to_dict()


wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)
wordcloud.generate_from_frequencies(frequencies=dict_freq)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("visualizacao_e2_g2_out/question1.png")

############################################################################################################

######  QUESTION 2  ######

dictionary = fe.concat_elements_column(df, 'name')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)

string = dictionary['all']
freq = fe.elements_freq(dictionary)
dict_freq = freq["all"].to_dict()

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)
wordcloud.generate_from_frequencies(frequencies=dict_freq)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("visualizacao_e2_g2_out/question2.png")

############################################################################################################

######  QUESTÃO 4  ######

dictionary = fe.concat_elements_column(df, 'lyrics')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)
dictionary = fe.remove_undesirables(dictionary)

string = " ".join(dictionary['all'])
freq = fe.elements_freq(dictionary)
dict_freq = freq["all"].to_dict()

wordcloud = WordCloud(background_color="black", width=1600, height=800).generate(string)
wordcloud.generate_from_frequencies(frequencies=dict_freq)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(wordcloud)
wordcloud.to_file("visualizacao_e2_g2_out/question4.png")
