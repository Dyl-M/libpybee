# -*- coding: utf-8 -*-

"""File Information
@file_name: print_all_tracks.py
@author: Dylan "dyl-m" Monfret
Example script: Display all library tracks
"""

import libpybee

MY_LIBRARY = libpybee.Library("../_tests/test_lib_01.xml")

# Use `tracks` attribute, the dictionary containing each track from MusicBee, to iterate over them.
for track in MY_LIBRARY.tracks.values():
    print(track)  # Output: [track.id] {track.artist} - {track.title}
