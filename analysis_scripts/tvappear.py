# Informações do IMDB

import pandas as pd
import sys

try:
    a_file = open("../data/tvappear.txt", "r")

except FileNotFoundError:
    print("tvappear.txt was not found in /data/. The file structure of the project is altered!")
    sys.exit(1)

lines = a_file.read().splitlines()

tv_dict = {}

for i in range(51):
    tv_dict[lines[2*i]] = lines[2*i+1]

a_file.close()

keysList = list(tv_dict.keys())

tv_pd = pd.DataFrame.from_dict(tv_dict, orient='index')

# Em quais TV shows essa música aparece?

def TV(song):
    song = '"'+song+'"'
    t = tv_pd[tv_pd.isin([song]).all(axis=1)]
    print(t)

# Quais TV shows têm alguma música do Arctic Monkeys?

def TVshows():
    for show in keysList:
        print(show)

# Quais músicas do Arctic Monkeys já apareceram nesse TV show?

def songsInShow(show):
    try:
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Series)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Movie documentary)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Mini Series)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Special)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Mini Series documentary)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (Documentary)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (Video short)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Series documentary)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (TV Movie)"
        print(tv_pd.loc[show])
    except KeyError:
        pass
    try:
        show = show + " (Video Game)"
        print(tv_pd.loc[show])
    except KeyError:
        pass

songsInShow("Top Gear")
TV("Reckless Serenade")
