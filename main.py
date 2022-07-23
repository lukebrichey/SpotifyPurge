from spotify_logic import edit_playlist

# Find playlist to be edited
init_prompt = "Please enter the name of the playlist you want to edit: \n"
playlist_name = input(init_prompt).lower()

# Find artist(s) that user wants to delete
artist_prompt = ("What artist(s) would you like to remove? \n"
                 "Note: For multiple artists, separate names using a comma "
                 "(i.e. Joji, Van Halen) \n")
artists = input(artist_prompt).lower().split(", ")

# Spotify logic
if edit_playlist(playlist_name, artists):
    # If true then edits succesfully made
    print("Success! Check out your playlist!")



