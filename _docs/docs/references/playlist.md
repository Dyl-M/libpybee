A class to store playlist information. [[⛓️‍💥 Source code]](https://github.com/Dyl-M/libpybee/blob/main/libpybee/Playlist.py)

## Class definition

### Initialize a Playlist object

```py
import libpybee

my_playlist = libpybee.Playlist(p_id='Y001')
print(my_playlist)
```

```cmd  title="Run output (with ID only)"
[<Playlist ID: Y001>] <Playlist Name: None>: <Number of tracks in the Playlist: 0> track(s).
```

| Parameter | Type  | Description                           |
|-----------|-------|---------------------------------------|
| `p_id`    | `str` | Playlist ID. Must not be used before. |

### Enriching a Playlist object

Redefine `name` and `n_tracks` attributes to output something else than `None` while calling `print` function on a playlist:

```py
import libpybee

my_playlist_2 = libpybee.Playlist(p_id='Y002')
my_playlist_2.name = "My Playlist"
my_playlist_2.n_tracks = 2

print(my_playlist_2)
```

```cmd  title="Run output"
[Y002] My Playlist: 2 tracks
```

* The same kind of manipulation can be performed to enrich the attributes listed afterward.
* That said, `Playlist` class has been designed to be used as part of a system working with [`Library`](library.md) and [`Track`](track.md) classes.

## Class variable

| Attributes      | Type  | Description                      |
|-----------------|-------|----------------------------------|
| `all_playlists` | `set` | Set containing all playlists' ID |

## Class attributes

| Attributes      | Type   | Description                                                             | Default value | Value by calling [`Library`](library.md)                                            |
|-----------------|--------|-------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------|
| `id`            | `str`  | Playlist Identifier                                                     | -             | XML tag `Playlist ID` with leading (optional) zeros                                 |
| `name`          | `str`  | Playlist Name                                                           | `None`        | XML tag `Name`                                                                      |
| `all_items`     | `bool` | [Unsure] Indicates whether all the music in the playlist really exists. | `None`        | XML tag `All Items`                                                                 |
| `persistent_id` | `str`  | Playlist Persistent Identifier (randomly generated string)              | `None`        | XML tag `Persistent ID`                                                             |
| `tracks`        | `list` | List of tracks included in the Playlist                                 | Empty list    | List of [`Track`](track.md) object based on information in `Playlist Items` XML tag |
| `n_tracks`      | `int`  | Number of tracks in the playlist                                        | 0             | `len(Playlist.tracks)` while calling [`Library`](library.md)                        |

- For now, the value of `n_tracks` is not directly attached to the actual number of tracks registered for a Playlist object. This will be fix in further version.
- Attributes that can be deleted due to a lack of coherent information:
    - `all_items`: Perhaps inherited from `libpytunes`? And seems to be always `True`.
    - `persistent_id`: Perhaps inherited from `libpytunes`? And seems to not exists.

## Methods

### `to_dict`

> Return all attributes (name and value) for a Playlist object as Python dictionary.

```py
import libpybee
import pprint as pp

my_playlist_3 = libpybee.Playlist(t_id='BR03')

my_playlist_3.name = 'Top 10 🇧🇷 Phonk'
my_playlist_3.n_tracks = 10

pp.pprint(my_playlist_3.to_dict())
```

```cmd  title="Run output"
{'all_items': None
 'id': 'BR03'
 'n_tracks': 10,
 'name': 'Top 10 🇧🇷 Phonk'
 'persistent_id': None
 'tracks': []}
```