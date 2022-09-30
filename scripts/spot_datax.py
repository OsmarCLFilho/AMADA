import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

arctic_uri = 'spotify:artist:7Ln80lUS6He07XvHI8qqHH'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

album_uris = pd.DataFrame(spotify.artist_albums(arctic_uri)["items"])
album_uris.sort_values(by='release_date', axis='index', inplace=True)
album_uris.drop_duplicates(subset="name", inplace=True)
album_uris.set_index("name", inplace=True)
album_uris.drop(index=["Favourite Worst Nightmare (Standard Version)","Live at the Royal Albert Hall"], inplace=True)

album_uris = album_uris["uri"]

track_columns = ["album", "name", "popularity", "duration_ms"]
audio_columns = ["tempo", "energy", "loudness", "speechiness", "instrumentalness"]
data_columns = track_columns.copy().extend(audio_columns)

main_dataframe = pd.DataFrame(columns=data_columns)

for alb_uri in album_uris:
    track_uris = pd.DataFrame(spotify.album_tracks(alb_uri)["items"])
    track_uris.set_index("name", inplace=True)

    track_uris = track_uris["uri"]

    for tra_uri in track_uris:
        print(tra_uri)
        track_data = pd.DataFrame([spotify.track(tra_uri)])[track_columns].join(pd.DataFrame(spotify.audio_features(tra_uri))[audio_columns])
        track_data.at[0, "album"] = track_data.at[0, "album"]["name"]

        main_dataframe = pd.concat(objs=[main_dataframe, track_data], axis="index")

main_dataframe[["album", "name"]] = main_dataframe[["album", "name"]].applymap(lambda string: string.upper().replace("…", "..."))
main_dataframe.set_index(["album", "name"], inplace=True)

main_dataframe.to_csv("../results/spot_data.csv")
