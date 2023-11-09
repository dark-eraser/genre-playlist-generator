import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
# Spotify API credential
def spotipy_client():
    with open('creds.json') as f:
        data = json.load(f)
        # client_credentials_manager = SpotifyClientCredentials(data["client_id"], data["client_secret"])
        # sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
        # return sp
        # print(data["client_id"])

        return spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=data['client_id'], 
            client_secret=data['client_secret'],
            scope="user-library-read",
            redirect_uri="http://localhost:8888/callback/"
            ))

def search_song(sp_client):

    print(sp_client.current_user())
    print(sp_client.current_user_saved_tracks(limit=5, offset=0))

if __name__ == "__main__":
    sp_client=spotipy_client()
    search_song(sp_client)