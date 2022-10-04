import seaborn as sns
import pandas as pd
import sys
sns.set_theme(style="ticks")

try:
    df = pd.read_csv('../results/final_dataset.csv')

except FileNotFoundError:
    print("final_dataset.csv not found in /results/. The file structure of the project is altered!")
    sys.exit(1)

df.loc[df["album"] == "WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT", "album"] = "WPSIATWIN"
df.loc[df["album"] == "FAVOURITE WORST NIGHTMARE", "album"] = "FWN"
df.loc[df["album"] == "SUCK IT AND SEE", "album"] = "SIAS"
df.loc[df["album"] == "TRANQUILITY BASE HOTEL & CASINO", "album"] = "TBHC"

df.sort_values(by="popularity", axis="index", inplace=True)

palette_color = sns.color_palette('bright')

alb_pop = sns.barplot(data=df, x="album", y="popularity")

alb_pop.figure.savefig("viz_g1_out/viz1_alb_pop.png")

alb_pop = sns.barplot(data=df, x="album", y="duration_ms")

alb_pop.figure.savefig("viz_g1_out/viz2_alb_dur.png")

alb_pop = sns.barplot(data=df, x="name", y="popularity")

alb_pop.figure.savefig("viz_g1_out/viz3_nam_pop.png")

alb_pop = sns.barplot(data=df, x="name", y="duration_ms")

alb_pop.figure.savefig("viz_g1_out/viz4_nam_dur.png")

alb_pop = sns.lmplot(data=df[df["popularity"] != 0], x="popularity", y="duration_ms")

alb_pop.figure.savefig("viz_g1_out/viz5_pop_dur.png")
