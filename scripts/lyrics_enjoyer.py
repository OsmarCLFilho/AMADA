import pandas as pd

with open("../data/lyrics.csv") as lyrics_file:
    lyrics_data = pd.read_csv(lyrics_file)

    lyrics_data.sort_values(by="album", axis="index", inplace=True)

    lyrics_data[["album", "name"]] = lyrics_data[["album", "name"]].applymap(lambda string: string.upper().replace("’","'"), na_action="ignore")
    lyrics_data.set_index(["album", "name"], inplace=True)

    with open("../results/spot_data.csv") as spot_file:
        spot_data = pd.read_csv(spot_file)

        spot_data.set_index(["album", "name"], inplace=True)

        final_data = lyrics_data.join(spot_data).sort_index(axis="index")
        (rows, columns) = final_data.shape

        for row in range(rows):
            print(final_data.iloc[row])

        final_data.to_csv(path_or_buf="../results/spo_lyr_data.csv")
