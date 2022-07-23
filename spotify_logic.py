import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private playlist-modify-public playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def edit_playlist(name, artists):
    # Find playlist for user under the name proviuded
    playlists = sp.current_user_playlists()["items"]
    deleted_track_ids = [] 

    # Search playlists for match
    for playlist in playlists:
        if playlist['name'].lower() == name:
            # Retrieve tracks from playlist
            track_items = sp.playlist_items(
                              playlist['uri'],
                              fields="items(track(artists(name), id))",
                              additional_types=['track']
                          )['items']
            
            deletions = 0

            # Search through tracks of playlist
            for track in track_items:
                track_artists = track['track']['artists']
                for artist in track_artists:
                    if artist['name'].lower() in artists:
                        deleted_track_ids.append(track['track']['id'])
                        deletions += 1

            # No deletions, artist must not be found
            if deletions == 0:
                print("Artist not found, please try again")
                return False
            else:
                sp.playlist_remove_all_occurrences_of_items(
                    playlist['uri'],
                    deleted_track_ids
                )
                print(f"There were {deletions} deletions made.")
                return True

    print("Playlist not found, please try again")
    return False
    
