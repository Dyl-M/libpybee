A class to store MusicBee Library information. [[⛓️‍💥 Source code]](https://github.com/Dyl-M/libpybee/blob/main/libpybee/Library.py)

## Class definition

```py
import libpybee

my_library = libpybee.Library(lib_path="path/to/xml_file.xml")
print(my_library)
```

```cmd  title="Run output"
- MusicBee Library Information -
* MusicBee Version: <MusicBee Application Version>
* Library ID: <Library ID>
* Library location: <MusicBee Folder>iTunes Music Library.xml
* Major Version: 1
* Minor Version: 1
* Number of tracks: <Number of tracks>
* Number of playlists: <Number of playlist>
* Number of playlist folders: <Number of playlist folders>
```

| Parameter  | Type  | Description                            |
|------------|-------|----------------------------------------|
| `lib_path` | `str` | Path to the MusicBee "iTunes" XML file |

## Class attributes

| Attributes         | Type   | Description                                                         | Value by calling the constructor                                                                                              |
|--------------------|--------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `lib_path`         | `str`  | Path to the MusicBee "iTunes" XML file                              | `lib_path` parameter                                                                                                          |
| `app_version`      | `str`  | MusicBee Version                                                    | XML tag `Application Version`                                                                                                 |
| `lib_id`           | `str`  | MusicBee Library Identifier                                         | XML tag `Library Persistent ID`                                                                                               |
| `major_version`    | `int`  | "1"                                                                 | XML tag `Major Version`                                                                                                       |
| `minor_version`    | `int`  | "1"                                                                 | XML tag `Minor Version`                                                                                                       |
| `music_folder`     | `str`  | Folder where MusicBee Tracks are stored                             | XML tag `Music Folder` with "file://localhost/" mention removed                                                               |
| `playlist_folders` | `dict` | Dictionary registering all playlist folders in the MusicBee library | **Dictionary description**: "Playlist Persistent ID" as key, [`Playlist`](playlist.md) object with other information as value |
| `playlists`        | `dict` | Dictionary registering all playlists in the MusicBee library        | **Dictionary description**: "Playlist ID" as key, [`Playlist`](playlist.md) object as value                                   |
| `tracks`           | `dict` | Dictionary registering all tracks in the MusicBee library           | **Dictionary description**: "Track ID" as key, [`Track`](track.md) object as value                                            |

## Notes

Calling the `Library` object will immediately start retrieving all tracks and playlists from the XML file passed as a parameter.

To date, there is 1 known problem preventing the library from loading correctly:

* A tag's value must be consistent with its type. Tags registered as "integer" inside the XML file (such as BPM, Track Number, Disc Count, etc.) must be filled with integers only.
