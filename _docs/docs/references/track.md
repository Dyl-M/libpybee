A class to store track information. [[⛓️‍💥 Source code]](https://github.com/Dyl-M/libpybee/blob/main/libpybee/Track.py)

## Class definition

### Initialize a Track object

```py
import libpybee

my_track = libpybee.Track(t_id='X001')
print(my_track)
```

```cmd  title="Run output (with ID only)"
[<Track ID: X001>] <Track Artist: None> - <Track Title: None>
```

| Parameter | Type  | Description                        |
|-----------|-------|------------------------------------|
| `t_id`    | `str` | Track ID. Must not be used before. |

### Enriching a Track object

Redefine `artist` and `title` attributes to output something else than `None` while calling `print` function on a track:

```py
import libpybee

# Simple Track constructor
my_track_1 = libpybee.Track(t_id='X001')

# Call to Track constructor and attribute setting
my_track_2 = libpybee.Track(t_id='X002')
my_track_2.artist = 'deadmau5'
my_track_2.title = 'Strobe'

print(my_track_1)
print(my_track_2)
```

```cmd  title="Run output"
[X001] None - None
[X002] deadmau5 - Strobe
```

* The same kind of manipulation can be performed to enrich the attributes listed afterward.
* That said, `Track` class has been designed to be used as part of a system working with [`Library`](library.md) and [`Playlist`](playlist.md) classes.

## Class variable

| Attributes   | Type  | Description                   |
|--------------|-------|-------------------------------|
| `all_tracks` | `set` | Set containing all tracks' ID |

## Class attributes

| Attributes        | Type       | Description                                                           | Default value | Value by calling [`Library`](library.md)                   |
|-------------------|------------|-----------------------------------------------------------------------|---------------|------------------------------------------------------------|
| `id`              | `str`      | Track Identifier                                                      | -             | XML tag `Track ID` with leading (optional) zeros           |
| `title`           | `str`      | Track Title                                                           | `None`        | XML tag `Title`                                            |
| `artist`          | `str`      | Track Artist (_Displayed Artist_)                                     | `None`        | XML tag `Artist`                                           |
| `album`           | `str`      | Track Album Title                                                     | `None`        | XML tag `Album`                                            |
| `album_artist`    | `str`      | Album Main Artist                                                     | `None`        | XML tag `Album Artist`                                     |
| `album_rating`    | `float`    | Album Rating                                                          | `None`        | XML tag `Album Rating`                                     |
| `artist_list`     | `list`     | Artists mentioned on the track (Main artists, Guests, Remixers, etc.) | Empty list    | XML tags `Artist1`, `Artist2`, etc. or simply `Artist` tag |
| `bitrate`         | `int`      | Track Bitrate                                                         | `None`        | XML tag `Bit Rate`                                         |
| `bpm`             | `int`      | Track Tempo in Beat Per Minute                                        | `None`        | XML tag `BPM`                                              |
| `comments`        | `str`      | Track Comments                                                        | `None`        | XML tag `Comment`                                          |
| `compilation`     | `bool`     | Indicate if the track is part of a compilation                        | `None`        | `True` if `Compilation` XML tag exists, `False` otherwise  |
| `composer`        | `str`      | Track Composer                                                        | `None`        | XML tag `Composer`                                         |
| `date_added`      | `datetime` | Track addition date to MusicBee Library                               | `None`        | XML tag `Date Added`                                       |
| `date_modified`   | `datetime` | Track latest modification date in MusicBee Library                    | `None`        | XML tag `Date Modified`                                    |
| `disc_count`      | `int`      | Amount of discs for the album                                         | `None`        | XML tag `Disc Count`                                       |
| `disc_number`     | `int`      | Disc' number in the album                                             | `None`        | XML tag `Disc Number`                                      |
| `encoder`         | `str`      | Track encoder                                                         | `None`        | XML tag `Encoder`                                          |
| `episode_date`    | `datetime` | Episode date, used for podcasts                                       | `None`        | XML tag `Episode Date`                                     |
| `file_location`   | `str`      | Track file location                                                   | `None`        | XML tag `Location`                                         |
| `genre`           | `str`      | Track Genre                                                           | `None`        | XML tags `Genre1`, `Genre2`, etc. or simply `Genre` tag    |
| `grouping`        | `list`     | Track Groups                                                          | `None`        | XML tag `Grouping` split by ";"                            |
| `kind`            | `str`      | Track Kind                                                            | `None`        | XML tag `Kind`                                             |
| `last_played`     | `datetime` | Track latest play date in MusicBee Library                            | `None`        | XML tag `Play Date UTC`                                    |
| `length`          | `int`      | Track Duration (in milliseconds)                                      | `None`        | XML tag `Total Time`                                       |
| `movement_count`  | `int`      | Amount of movements in the album                                      | `None`        | XML tag `Movement Count`                                   |
| `movement_name`   | `str`      | Track movement name                                                   | `None`        | XML tag `Movement Name`                                    |
| `movement_number` | `int`      | Track movement number                                                 | `None`        | XML tag `Movement Number`                                  |
| `play_count`      | `int`      | Track Play Count                                                      | 0             | XML tag `Play Count`                                       |
| `persistent_id`   | `str`      | Track Persistent Identifier (randomly generated string)               | `None`        | XML tag `Persistent ID`                                    |
| `rating`          | `int`      | Track individual Rating                                               | `None`        | XML tag `Rating`                                           |
| `release_date`    | `str`      | Track Release Date                                                    | `None`        | XML tag `Original Year`                                    |
| `sample_rate`     | `int`      | Track Sample Rate                                                     | `None`        | XML tag `Sample Rate`                                      |
| `skip_count`      | `int`      | Track Skip Count                                                      | 0             | XML tag `Skip Count`                                       |
| `skip_date`       | `datetime` | Track latest skip date in MusicBee Library                            | `None`        | XML tag `Skip Date`                                        |
| `track_count`     | `int`      | Amount of track in the album                                          | `None`        | XML tag `Track Count`                                      |
| `track_number`    | `int`      | Track number in the album                                             | `None`        | XML tag `Track Number`                                     |
| `track_type`      | `str`      | Track Type                                                            | `None`        | XML tag `Track Type`                                       |
| `size`            | `int`      | Track size (in byte)                                                  | `None`        | XML tag `Size`                                             |
| `work`            | `str`      | Track Work                                                            | `None`        | XML tag `Work`                                             |
| `year`            | `int`      | Track Year                                                            | `None`        | XML tag `Year`                                             |

- The `release_date` attribute will not be a `datetime`, since the format of "Original Year" tag may vary from one user to another.
- Attributes that can be deleted due to no entry available in MusicBee:
    - `episode_date`: Perhaps inherited from `libpytunes`?

## Methods

### `to_dict`

> Return all attributes (name and value) for a Track object as Python dictionary.

```py
import libpybee
import pprint as pp

my_track_3 = libpybee.Track(t_id='X003')

my_track_3.artist = 'Rick Astley'
my_track_3.title = 'Never Gonna Give You Up'
my_track_3.genre = 'Pop'

pp.pprint(my_track_3.to_dict())
```

```cmd  title="Run output"
{'album': None
 ...
 'artist': 'Rick Astley',
 ...
 'genre': 'Pop',
 ...
 'id': 'X003',
 ...
 'year': None}
```