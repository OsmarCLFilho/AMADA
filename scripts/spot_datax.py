import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

arctic_uri = 'spotify:artist:7Ln80lUS6He07XvHI8qqHH'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

album_uris = pd.DataFrame(spotify.artist_albums(arctic_uri, album_type='album')["items"])
album_uris.sort_values(by='release_date', axis='index', inplace=True)
album_uris.drop_duplicates(subset="name", inplace=True)
album_uris.set_index("name", inplace=True)
album_uris.drop(index=["Favourite Worst Nightmare (Standard Version)","Live at the Royal Albert Hall"], inplace=True)

album_uris = album_uris["uri"]

main_dataframe = pd.DataFrame(columns=["album", "name", "popularity", "duration_ms"])

for alb_uri in album_uris:
    track_uris = pd.DataFrame(spotify.album_tracks(alb_uri)["items"])
    track_uris.set_index("name", inplace=True)

    track_uris = track_uris["uri"]

    for tra_uri in track_uris:
        print(tra_uri)
        full_track_data = pd.DataFrame([spotify.track(tra_uri)])
        full_track_data.at[0, "album"] = full_track_data.at[0, "album"]["name"]
        
        final_track_data = full_track_data[["album","name","popularity","duration_ms"]]

        main_dataframe = pd.concat(objs=[main_dataframe, final_track_data], axis="index")

final_index = pd.MultiIndex.from_frame(main_dataframe[["album","name"]])

main_dataframe.drop(["album","name"], axis="columns", inplace=True)
main_dataframe.set_index(final_index, inplace=True)

main_dataframe.to_csv("../results/spot_data.csv")
