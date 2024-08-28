# -*- coding: utf-8 -*-

"""File Information
@file_name: get_all_artist_tracks.py
@author: Dylan "dyl-m" Monfret
Example script: Get all tracks mentioning a specified artists
"""

import libpybee

MY_LIBRARY = libpybee.Library(lib_path="../_tests/test_lib_01.xml")

target_artist = 'RetroVision'  # Looking for RetroVision's release in my MusicBee library

# Iterating over tracks and looking for 'RetroVision' in `artist_list` for each of them
retro_tracks = [track for track in MY_LIBRARY.tracks.values() if target_artist in track.artist_list]

print(retro_tracks)  # Output: list of Track object

for retro_t in retro_tracks:
    print(retro_t.title)  # Output: Each RetroVision's tracks name, featuring and remixes included
