import pandas as pd
import sys

try:
    AM =  pd.read_csv('../results/final_dataset.csv')

except FileNotFoundError:
    print("final_dataset.csv was not found in /results/. The file structure of the project is altered!")
    sys.exit(1)

wpsiatwin_df = AM.loc[AM['album'] == "WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT"]
fwn_df = AM.loc[AM['album'] == 'FAVOURITE WORST NIGHTMARE']
humbug_df = AM.loc[AM['album'] == 'HUMBUG']
sias_df = AM.loc[AM['album'] == 'SUCK IT AND SEE']
am_df = AM.loc[AM['album'] == 'AM']
tbhc_df = AM.loc[AM['album'] == 'TRANQUILITY BASE HOTEL & CASINO']

wpsiatwin_popularity = wpsiatwin_df["popularity"]
wpsiatwin_duration_ms = wpsiatwin_df["duration_ms"]

fwn_popularity = fwn_df["popularity"]
fwn_duration_ms = fwn_df["duration_ms"]

humbug_popularity = humbug_df["popularity"]
humbug_duration_ms = humbug_df["duration_ms"]

sias_popularity = sias_df["popularity"]
sias_duration_ms = sias_df["duration_ms"]

am_popularity = am_df["popularity"]
am_duration_ms = am_df["duration_ms"]

tbhc_popularity = tbhc_df["popularity"]
tbhc_duration_ms = tbhc_df["duration_ms"]

AM_popularity = AM["popularity"]
AM_duration_ms = AM["duration_ms"]

def popularity(album):
    if album == "WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT":
        i = wpsiatwin_popularity.argmax()
        j = wpsiatwin_popularity.argmin()
        maxsong = wpsiatwin_df['name'].loc[wpsiatwin_df.index[i]]
        minsong = wpsiatwin_df['name'].loc[wpsiatwin_df.index[j]]
        print("Most popular track:", maxsong)
        print("Least popular track:", minsong)
    if album == 'FAVOURITE WORST NIGHTMARE':
        i = fwn_popularity.argmax()
        j = fwn_popularity.argmin()
        maxsong = fwn_df['name'].loc[fwn_df.index[i]]
        minsong = fwn_df['name'].loc[fwn_df.index[j]]
        print("Most popular track:", maxsong)
        print("Least popular track:", minsong)
    if album == 'HUMBUG':
        i = humbug_popularity.argmax()
        j = humbug_popularity.argmin()
        maxsong = humbug_df['name'].loc[humbug_df.index[i]]
        minsong = humbug_df['name'].loc[humbug_df.index[j]]
        print("Most popular track:", maxsong)
        print("Least popular track:", minsong)
    if album == 'SUCK IT AND SEE':
        i = sias_popularity.argmax()
        j = sias_popularity.argmin()
        maxsong = sias_df['name'].loc[sias_df.index[i]]
        minsong = sias_df['name'].loc[sias_df.index[j]]
        print("Most popular track:", maxsong)
        print("Least popular track:", minsong)
    if album == 'AM':
        i = am_popularity.argmax()
        j = am_popularity.argmin()
        maxsong = am_df['name'].loc[am_df.index[i]]
        minsong = am_df['name'].loc[am_df.index[j]]
        print("Most popular track:", maxsong)
        print("Least popular track:", minsong)
    if album == 'TRANQUILITY BASE HOTEL & CASINO':
        i = tbhc_popularity.argmax()
        j = tbhc_popularity.argmin()
        maxsong = tbhc_df['name'].loc[tbhc_df.index[i]]
        minsong = tbhc_df['name'].loc[tbhc_df.index[j]]
        print("Most popular track:", maxsong)
        print("Least popular track:", minsong)

def duration(album):
    if album == "WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT":
        i = wpsiatwin_duration_ms.argmax()
        j = wpsiatwin_duration_ms.argmin()
        maxsong = wpsiatwin_df['name'].loc[wpsiatwin_df.index[i]]
        minsong = wpsiatwin_df['name'].loc[wpsiatwin_df.index[j]]
        print("Longest track:", maxsong)
        print("Shortest track:", minsong)
    if album == 'FAVOURITE WORST NIGHTMARE':
        i = fwn_duration_ms.argmax()
        j = fwn_duration_ms.argmin()
        maxsong = fwn_df['name'].loc[fwn_df.index[i]]
        minsong = fwn_df['name'].loc[fwn_df.index[j]]
        print("Longest track:", maxsong)
        print("Shortest track:", minsong)
    if album == 'HUMBUG':
        i = humbug_duration_ms.argmax()
        j = humbug_duration_ms.argmin()
        maxsong = humbug_df['name'].loc[humbug_df.index[i]]
        minsong = humbug_df['name'].loc[humbug_df.index[j]]
        print("Longest track:", maxsong)
        print("Shortest track:", minsong)
    if album == 'SUCK IT AND SEE':
        i = sias_duration_ms.argmax()
        j = sias_duration_ms.argmin()
        maxsong = sias_df['name'].loc[sias_df.index[i]]
        minsong = sias_df['name'].loc[sias_df.index[j]]
        print("Longest track:", maxsong)
        print("Shortest track:", minsong)
    if album == 'AM':
        i = am_duration_ms.argmax()
        j = am_duration_ms.argmin()
        maxsong = am_df['name'].loc[am_df.index[i]]
        minsong = am_df['name'].loc[am_df.index[j]]
        print("Longest track:", maxsong)
        print("Shortest track:", minsong)
    if album == 'TRANQUILITY BASE HOTEL & CASINO':
        i = tbhc_duration_ms.argmax()
        j = tbhc_duration_ms.argmin()
        maxsong = tbhc_df['name'].loc[tbhc_df.index[i]]
        minsong = tbhc_df['name'].loc[tbhc_df.index[j]]
        print("Longest track:", maxsong)
        print("Shortest track:", minsong)

def allpopularity():
    i = AM_popularity.argmax()
    j = AM_popularity.argmin()
    maxsong = AM['name'].loc[AM.index[i]]
    minsong = AM['name'].loc[AM.index[j]]
    print("Most popular track overall: ", maxsong)
    print("Least popular track overall: ", minsong)

def allduration():
    i = AM_duration_ms.argmax()
    j = AM_duration_ms.argmin()
    maxsong = AM['name'].loc[AM.index[i]]
    minsong = AM['name'].loc[AM.index[j]]
    print("Longest track overall:", maxsong)
    print("Shortest track overall:", minsong)

def awards():
    print("Highest number of Gold Certifications: WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT (5)")
    print("Higuest number of Platinum Certifications: AM (12)")

def correlation():
    col1, col2 = "duration_ms", "popularity"
    corr = AM[col1].corr(AM[col2])
    print("The correlation between", col1, "and", col2, "is:", round(corr, 2))

if __name__ == "__main__":
    print("-----\nPopularity:")
    print("Whatever People Say...")
    popularity("WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT")
    print("Favourite Worst Nightmare")
    popularity("FAVOURITE WORST NIGHTMARE")
    print("Humbug")
    popularity("HUMBUG")
    print("Suck It And See")
    popularity("SUCK IT AND SEE")
    print("AM")
    popularity("AM")
    print("Tranquility Base Hotel & Casino")
    popularity("TRANQUILITY BASE HOTEL & CASINO")

    print("-----\nDuration:")
    print("Whatever People Say...")
    duration("WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT")
    print("Favourite Worst Nightmare")
    duration("FAVOURITE WORST NIGHTMARE")
    print("Humbug")
    duration("HUMBUG")
    print("Suck It And See")
    duration("SUCK IT AND SEE")
    print("AM")
    duration("AM")
    print("Tranquility Base Hotel & Casino")
    duration("TRANQUILITY BASE HOTEL & CASINO")

    print("-----\nPopularity all Albums:")
    allpopularity()

    print("-----\nDuration all Albums:")
    allduration()

    print("-----\nAwards:")
    awards()

    print("-----\nCorrelation:")
    correlation()
