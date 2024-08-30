Overview of the possibilities offered by `libpybee` and its various features.

Keep in mind that the [`Library`](references/library.md) class is central to working with your MusicBee library. It provides access to tracks and playlists easily.

## Display all library tracks

This example shows how to iterate over all tracks in the library and print out basic information for each track.

```py
import libpybee

MY_LIBRARY = libpybee.Library("iTunes Library.xml")

# Use `tracks` attribute, the dictionary containing each track from MusicBee, to iterate over them.
for track in MY_LIBRARY.tracks.values():
    print(track)  # Output: [track.id] {track.artist} - {track.title}
```

📄 References: [`Library`](references/library.md), [`Track`](references/track.md)

## Get all tracks mentioning a specified artists

This example shows how to retrieve each tracks where a specific artist is mentioned.

```py
import libpybee

MY_LIBRARY = libpybee.Library("iTunes Library.xml")

target_artist = 'RetroVision'  # Looking for RetroVision's release in my MusicBee library

# Iterating over tracks and looking for 'RetroVision' in `artist_list` for each of them
retro_tracks = [track for track in MY_LIBRARY.tracks.values() if target_artist in track.artist_list]

print(retro_tracks)  # Output: list of Track object

for retro_t in retro_tracks:
    print(retro_t.title)  # Output: Each RetroVision's tracks name, featuring and remixes included
```

📄 References: [`Library`](references/library.md), [`Track`](references/track.md)

## Export the library (tracks & playlists) to JSON file

This example shows how to export your tracks and playlists as a JSON file.

```py
import json
import libpybee

MY_LIBRARY = libpybee.Library("iTunes Library.xml")

# List all tracks and playlists, convert each of them to dictionary
exp_dict = {'Tracks': [track.to_dict() for track in MY_LIBRARY.tracks.values()],
            'Playlists': [playlist.to_dict() for playlist in MY_LIBRARY.playlists.values()]}

# Export as JSON
with open('lib.json', 'w', encoding='utf8') as json_file:
    # "default" parameter set to `str` is mandatory to manage complex values (such as 'datetime' values and Track objects in playlists)
    json.dump(exp_dict, json_file, indent=4, default=str) 
```

📄 References: [`Library`](references/library.md), [`Track`](references/track.md), [`Playlist`](references/playlist.md)

## Export all tracks of a playlist as a CSV file

This example shows how to all your tracks as a CSV file, considering "Artists" and "Track Title" only.

```py
import libpybee
import pandas as pd

MY_LIBRARY = libpybee.Library("iTunes Library.xml")

# Retrieve first playlist
pl_0 = list(MY_LIBRARY.playlists.values())[0]

# Keep Track Artist and Title
tracks = [{'artist': track.artist, 'title': track.title} for track in pl_0.tracks]

# Export with `pandas`
pd.DataFrame(tracks).to_csv("playlist_0.csv")
```

📄 References: [`Library`](references/library.md), [`Track`](references/track.md), [`Playlist`](references/playlist.md)

## Display all playlists with their folder

This example shows how to iterate over all playlist folders and their playlists in the library.

```py
import libpybee

MY_LIB = libpybee.Library('iTunes Library.xml')
folders = MY_LIB.playlist_folders

for _, folder in folders.items():
    print(f'FOLDER: {folder["folder_name"]}')

    for playlist in folder['playlists']:
        print(playlist)
```

📄 References: [`Library`](references/library.md), [`Playlist`](references/playlist.md)