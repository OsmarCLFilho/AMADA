import pandas as pd

with open("../data/lyrics.csv") as csv_file:
    main_data = pd.read_csv(csv_file)

    main_data.sort_values(by="album", axis="index", inplace=True)

    new_index = pd.MultiIndex.from_frame(main_data[["album", "name"]])

    main_data.set_index(new_index, inplace=True)
    main_data.drop(labels=["album","name"], axis="columns", inplace=True)

    main_data.to_csv(path_or_buf="../results/alb_lyrics.csv", na_rep="None")
