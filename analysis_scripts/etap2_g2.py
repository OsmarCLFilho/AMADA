import func_etapa2_g2 as fe
import pandas as pd
import copy
import sys

try:
    df = pd.read_csv("../results/final_dataset.csv")

except FileNotFoundError:
    print("final_dataset.csv was not found in /results/. The file structure of the project is altered!")
    sys.exit(1)

print("######  QUESTION 1  ######\n")

dictionary = fe.concat_elements_column(df, 'album')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)
dictionary = fe.elements_freq(dictionary)

print("10 most common words in the album titles:\n")
print(dictionary['all'].head(10))

print("\n\n")


print("######  QUESTION 2  ######\n")

dictionary = fe.concat_elements_column(df, 'name')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)
dictionary = fe.elements_freq(dictionary)

print("10 most common words in the track titles:\n")
print(dictionary['all'].head(10))

print("\n\n")


print("######  QUESTION 3  ######\n")

dictionary = fe.concat_elements_column(df, 'lyrics', 'album')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)
dictionary = fe.remove_undesirables(dictionary)
dictionary = fe.elements_freq(dictionary)

print("10 most common words in the lyrics per album:\n")

for key in dictionary.keys():
    print(key,":")
    if isinstance(dictionary[key], str):
        print(dictionary[key])
    else:
        print(dictionary[key].head(10))
    print("\n")

print("\n\n")

print("######  QUESTION 4  ######\n")

dictionary = fe.concat_elements_column(df, 'lyrics')
dictionary = fe.remove_contractions(dictionary)
dictionary = fe.remove_characters(dictionary)
dictionary = fe.remove_undesirables(dictionary)
dictionary = fe.elements_freq(dictionary)

print("10 most common words in the lyrics:\n")
print(dictionary['all'].head(10))

print("\n\n")

print("######  QUESTION 5  ######\n")

dictionary = fe.concat_elements_column(df, 'lyrics', 'album')
dictionary = fe.relevancy(dictionary)

print("Amount of times that the albums titles show up in the lyrics\n")
print("(albums whose lyrics were not found were removed):\n")

for key in copy.deepcopy(dictionary).keys():
    if isinstance(dictionary[key], str):
        dictionary.pop(key)

for ind in sorted(dictionary, key = dictionary.get, reverse=True):
    print(ind, ": ", dictionary[ind])

print("\n\n")


print("######  QUESTION 6  ######\n")

dictionary = fe.concat_elements_column(df, 'lyrics', 'name')
dictionary = fe.relevancy(dictionary)

print("Amount of times that the tracks titles show up in the lyrics\n")
print("(tracks whose lyrics were not found were removed):")

for key in copy.deepcopy(dictionary).keys():
    if isinstance(dictionary[key], str):
        dictionary.pop(key)

for ind in sorted(dictionary, key = dictionary.get, reverse=True):
    print(ind, ": ", dictionary[ind])
