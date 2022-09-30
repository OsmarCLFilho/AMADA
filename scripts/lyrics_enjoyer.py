import pandas as pd

with open("../data/lyrics.csv") as lyrics_file:
    lyrics_data = pd.read_csv(lyrics_file)

    lyrics_data.sort_values(by="album", axis="index", inplace=True)

    lyrics_data[["album", "name"]] = lyrics_data[["album", "name"]].applymap(lambda string: string.upper().replace("’","'"), na_action="ignore")
    lyrics_data.set_index(["album", "name"], inplace=True)

    with open("../results/spot_data.csv") as spot_file:
        spot_data = pd.read_csv(spot_file)

        spot_data.set_index(["album", "name"], inplace=True)

        print(spot_data.loc["WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT"])
        print(lyrics_data.loc["WHATEVER PEOPLE SAY I AM, THAT'S WHAT I'M NOT"])

        final_data = spot_data.join(lyrics_data).sort_index(axis="index")

        final_data.to_csv("../results/spo_lyr_data.csv", na_rep="_IGNORE_EMPTY_IGNORE_")
        final_data.to_html("spo_lyr_data.html", na_rep="_IGNORE_EMPTY_IGNORE_")
