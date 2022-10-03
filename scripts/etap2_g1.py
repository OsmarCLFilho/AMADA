import pandas as pd

AM =  pd.read_csv('final_dataset.csv')

AM.columns = ['Álbum', 'Música', 'Views', 'Duração']

wpsiatwin_df = AM.loc[AM['Álbum'] == "Whatever People Say I Am, That's What I'm Not"]
fwn_df = AM.loc[AM['Álbum'] == 'Favourite Worst Nightmare']
humbug_df = AM.loc[AM['Álbum'] == 'Humbug']
sias_df = AM.loc[AM['Álbum'] == 'Suck It and See']
am_df = AM.loc[AM['Álbum'] == 'AM']
tbhc_df = AM.loc[AM['Álbum'] == 'Tranquility Base Hotel & Casino']

wpsiatwin_views = wpsiatwin_df["Views"]
wpsiatwin_duration = wpsiatwin_df["Duração"]

fwn_views = fwn_df["Views"]
fwn_duration = fwn_df["Duração"]

humbug_views = humbug_df["Views"]
humbug_duration = humbug_df["Duração"]

sias_views = sias_df["Views"]
sias_duration = sias_df["Duração"]

am_views = am_df["Views"]
am_duration = am_df["Duração"]

tbhc_views = tbhc_df["Views"]
tbhc_duration = tbhc_df["Duração"]

AM_views = AM["Views"]
AM_duration = AM["Duração"]

def views(album):
    if album == "Whatever People Say I Am, That's What I'm Not":
        i = wpsiatwin_views.argmax()
        j = wpsiatwin_views.argmin()
        maxsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[i]]
        minsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[j]]
        print("Música mais ouvida:", maxsong)
        print("Música menos ouvida:", minsong)
    if album == 'Favourite Worst Nightmare':
        i = fwn_views.argmax()
        j = fwn_views.argmin()
        maxsong = fwn_df['Música'].loc[fwn_df.index[i]]
        minsong = fwn_df['Música'].loc[fwn_df.index[j]]
        print("Música mais ouvida:", maxsong)
        print("Música menos ouvida:", minsong)
    if album == 'Humbug':
        i = humbug_views.argmax()
        j = humbug_views.argmin()
        maxsong = humbug_df['Música'].loc[humbug_df.index[i]]
        minsong = humbug_df['Música'].loc[humbug_df.index[j]]
        print("Música mais ouvida:", maxsong)
        print("Música menos ouvida:", minsong)
    if album == 'Suck It and See':
        i = sias_views.argmax()
        j = sias_views.argmin()
        maxsong = sias_df['Música'].loc[sias_df.index[i]]
        minsong = sias_df['Música'].loc[sias_df.index[j]]
        print("Música mais ouvida:", maxsong)
        print("Música menos ouvida:", minsong)
    if album == 'AM':
        i = am_views.argmax()
        j = am_views.argmin()
        maxsong = am_df['Música'].loc[am_df.index[i]]
        minsong = am_df['Música'].loc[am_df.index[j]]
        print("Música mais ouvida:", maxsong)
        print("Música menos ouvida:", minsong)
    if album == 'Tranquility Base Hotel & Casino':
        i = tbhc_views.argmax()
        j = tbhc_views.argmin()
        maxsong = tbhc_df['Música'].loc[tbhc_df.index[i]]
        minsong = tbhc_df['Música'].loc[tbhc_df.index[j]]
        print("Música mais ouvida:", maxsong)
        print("Música menos ouvida:", minsong)

def durations(album):
    if album == "Whatever People Say I Am, That's What I'm Not":
        i = wpsiatwin_duration.argmax()
        j = wpsiatwin_duration.argmin()
        maxsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[i]]
        minsong = wpsiatwin_df['Música'].loc[wpsiatwin_df.index[j]]
        print("Música mais longa:", maxsong)
        print("Música mais curta:", minsong)
    if album == 'Favourite Worst Nightmare':
        i = fwn_duration.argmax()
        j = fwn_duration.argmin()
        maxsong = fwn_df['Música'].loc[fwn_df.index[i]]
        minsong = fwn_df['Música'].loc[fwn_df.index[j]]
        print("Música mais longa:", maxsong)
        print("Música mais curta:", minsong)
    if album == 'Humbug':
        i = humbug_duration.argmax()
        j = humbug_duration.argmin()
        maxsong = humbug_df['Música'].loc[humbug_df.index[i]]
        minsong = humbug_df['Música'].loc[humbug_df.index[j]]
        print("Música mais longa:", maxsong)
        print("Música mais curta:", minsong)
    if album == 'Suck It and See':
        i = sias_duration.argmax()
        j = sias_duration.argmin()
        maxsong = sias_df['Música'].loc[sias_df.index[i]]
        minsong = sias_df['Música'].loc[sias_df.index[j]]
        print("Música mais longa:", maxsong)
        print("Música mais curta:", minsong)
    if album == 'AM':
        i = am_duration.argmax()
        j = am_duration.argmin()
        maxsong = am_df['Música'].loc[am_df.index[i]]
        minsong = am_df['Música'].loc[am_df.index[j]]
        print("Música mais longa:", maxsong)
        print("Música mais curta:", minsong)
    if album == 'Tranquility Base Hotel & Casino':
        i = tbhc_duration.argmax()
        j = tbhc_duration.argmin()
        maxsong = tbhc_df['Música'].loc[tbhc_df.index[i]]
        minsong = tbhc_df['Música'].loc[tbhc_df.index[j]]
        print("Música mais longa:", maxsong)
        print("Música mais curta:", minsong)

def allviews():
    i = AM_views.argmax()
    j = AM_views.argmin()
    maxsong = AM['Música'].loc[AM.index[i]]
    minsong = AM['Música'].loc[AM.index[j]]
    print("Música mais ouvida no geral: ", maxsong)
    print("Música menos ouvida no geral: ", minsong)

def allduration():
    i = AM_duration.argmax()
    j = AM_duration.argmin()
    maxsong = AM['Música'].loc[AM.index[i]]
    minsong = AM['Música'].loc[AM.index[j]]
    print("Música mais longa no geral:", maxsong)
    print("Música mais curta no geral:", minsong)

def premios():
    print("Maior número de Gold Certifications: Whatever People Say I Am, That's What I'm Not (5)")
    print("Maior número de Platinum Certifications: AM (12)")

def correlation():
    col1, col2 = "Duração", "Views"
    corr = AM[col1].corr(AM[col2])
    print("A correlação entre", col1, "e", col2, "é:", round(corr, 2))
