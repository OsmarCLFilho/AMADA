import pandas as pd

wpsiatwin_df = AM.loc[AM['Álbum'] == "Whatever People Say I Am, That's What I'm Not"]
fwn_df = AM.loc[AM['Álbum'] == 'Favourite Worst Nightmare']
humbug_df = AM.loc[AM['Álbum'] == 'Humbug']
sias_df = AM.loc[AM['Álbum'] == 'Suck It and See']
am_df = AM.loc[AM['Álbum'] == 'AM']
tbhc_df = AM.loc[AM['Álbum'] == 'Tranquility Base Hotel & Casino']

wpsiatwin_views = wpsiatwin_df["Views"]
wpsiatwin_duration = wpsiatwin_duration["Duração"]
wpsiatwin_prizes = wpsiatwin_prizes["Prêmios"]

fwn_views = fwn_df["Views"]
fwn_duration = fwn_duration["Duração"]
fwn_prizes = fwn_prizes["Prêmios"]

humbug_views = humbug_df["Views"]
humbug_duration = humbug_duration["Duração"]
humbug_prizes = humbug_prizes["Prêmios"]

sias_views = sias_df["Views"]
sias_duration = sias_duration["Duração"]
sias_prizes = sias_prizes["Prêmios"]

am_views = am_df["Views"]
am_duration = am_duration["Duração"]
am_prizes = am_prizes["Prêmios"]

tbhc_views = tbhc_df["Views"]
tbhc_duration = tbhc_duration["Duração"]
tbhc_prizes = tbhc_prizes["Prêmios"]

AM_views = AM["Views"]
AM_duration = AM["Duração"]

def views(album):
    if album == "Whatever People Say I Am, That's What I'm Not":
        i = wpsiatwin_views.idmax()
        j = wpsiatwin_views.idmin()
        maxsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[i]]
        minsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[j]]
        return("Música mais ouvida:", maxsong)
        return("Música menos ouvida:", minsong)
    if album == 'Favourite Worst Nightmare':
        i = fwn_views.idmax()
        j = fwn_views.idmin()
        maxsong = fwn_df['Música'].loc[fwn_df.index[i]]
        minsong = fwn_df['Música'].loc[fwn_df.index[j]]
        return("Música mais ouvida:", maxsong)
        return("Música menos ouvida:", minsong)
    if album == 'Humbug':
        i = humbug_views.idmax()
        j = humbug_views.idmin()
        maxsong = humbug_df['Música'].loc[humbug_df.index[i]]
        minsong = humbug_df['Música'].loc[humbug_df.index[j]]
        return("Música mais ouvida:", maxsong)
        return("Música menos ouvida:", minsong)
    if album == 'Suck It and See':
        i = sias_views.idmax()
        j = sias_views.idmin()
        maxsong = sias_df['Música'].loc[sias_df.index[i]]
        minsong = sias_df['Música'].loc[sias_df.index[j]]
        return("Música mais ouvida:", maxsong)
        return("Música menos ouvida:", minsong)
    if album == 'AM':
        i = am_views.idmax()
        j = am_views.idmin()
        maxsong = am_df['Música'].loc[am_df.index[i]]
        minsong = am_df['Música'].loc[am_df.index[j]]
        return("Música mais ouvida:", maxsong)
        return("Música menos ouvida:", minsong)
    if album == 'Tranquility Base Hotel & Casino':
        i = tbhc_views.idmax()
        j = tbhc_views.idmin()
        maxsong = tbhc_df['Música'].loc[tbhc_df.index[i]]
        minsong = tbhc_df['Música'].loc[tbhc_df.index[j]]
        return("Música mais ouvida:", maxsong)
        return("Música menos ouvida:", minsong)

def durations(album):
    if album == "Whatever People Say I Am, That's What I'm Not":
        i = wpsiatwin_duration.idmax()
        j = wpsiatwin_duration.idmin()
        maxsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[i]]
        minsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[j]]
        return("Música mais longa:", maxsong)
        return("Música mais curta:", minsong)
    if album == 'Favourite Worst Nightmare':
        i = fwn_duration.idmax()
        j = fwn_duration.idmin()
        maxsong = fwn_df['Música'].loc[fwn_df.index[i]]
        minsong = fwn_df['Música'].loc[fwn_df.index[j]]
        return("Música mais longa:", maxsong)
        return("Música mais curta:", minsong)
    if album == 'Humbug':
        i = humbug_duration.idmax()
        j = humbug_duration.idmin()
        maxsong = humbug_df['Música'].loc[humbug_df.index[i]]
        minsong = humbug_df['Música'].loc[humbug_df.index[j]]
        return("Música mais longa:", maxsong)
        return("Música mais curta:", minsong)
    if album == 'Suck It and See':
        i = sias_duration.idmax()
        j = sias_duration.idmin()
        maxsong = sias_df['Música'].loc[sias_df.index[i]]
        minsong = sias_df['Música'].loc[sias_df.index[j]]
        return("Música mais longa:", maxsong)
        return("Música mais curta:", minsong)
    if album == 'AM':
        i = am_duration.idmax()
        j = am_duration.idmin()
        maxsong = am_df['Música'].loc[am_df.index[i]]
        minsong = am_df['Música'].loc[am_df.index[j]]
        return("Música mais longa:", maxsong)
        return("Música mais curta:", minsong)
    if album == 'Tranquility Base Hotel & Casino':
        i = tbhc_duration.idmax()
        j = tbhc_duration.idmin()
        maxsong = tbhc_df['Música'].loc[tbhc_df.index[i]]
        minsong = tbhc_df['Música'].loc[tbhc_df.index[j]]
        return("Música mais longa:", maxsong)
        return("Música mais curta:", minsong)

def allviews():
    i = AM_views.idmax()
    j = AM_views.idmin()
    maxsong = AM['Música'].loc[AM.index[i]]
    minsong = AM['Música'].loc[AM.index[j]]
    return("Música mais ouvida no geral: ", maxsong)
    return("Música menos ouvida no geral: ", minsong)

def allduration():
    i = AM_duration.idmax()
    j = AM_duration.idmin()
    maxsong = AM['Música'].loc[AM.index[i]]
    minsong = AM['Música'].loc[AM.index[j]]
    return("Música mais longa no geral:", maxsong)
    return("Música mais curta no geral:", minsong)

def correlation():
    col1, col2 = "Duração", "Música"
    corr = AM[col1].corr(AM[col2])
    print("A correlação entre", col1, "e", col2, "é:", round(corr, 2))