import seaborn as sns
import pandas as pd
sns.set_theme(style="ticks")

df = pd.read_csv('AM.csv')

df.loc[df["album"] == "Whatever People Say I Am, That's What I'm Not", "album"] = "WPSIATWIN"
df.loc[df["album"] == "Favourite Worst Nightmare", "album"] = "FWN"
df.loc[df["album"] == "Suck It and See", "album"] = "SIAS"
df.loc[df["album"] == "Tranquility Base Hotel & Casino", "album"] = "TBHC"

palette_color = sns.color_palette('bright')

alb_pop = sns.barplot(data=df, x="album", y="popularity")

alb_pop.figure.savefig("viz1_alb_pop.png")

alb_pop = sns.barplot(data=df, x="album", y="duration_ms")

alb_pop.figure.savefig("viz2_alb_dur.png")

alb_pop = sns.barplot(data=df, x="name", y="popularity")

alb_pop.figure.savefig("viz3_nam_pop.png")

alb_pop = sns.barplot(data=df, x="name", y="duration_ms")

alb_pop.figure.savefig("viz4_nam_dur.png")

alb_pop = sns.lmplot(data=df, x="popularity", y="duration_ms")

alb_pop.figure.savefig("viz5_pop_dur.png")