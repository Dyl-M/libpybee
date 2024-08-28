# -*- coding: utf-8 -*-

"""File Information
@file_name: export_as_csv.py
@author: Dylan "dyl-m" Monfret
Example script: Display all library tracks
"""

import libpybee
import pandas as pd

MY_LIBRARY = libpybee.Library(lib_path="../_tests/test_lib_01.xml")

# Retrieve first playlist
pl_1 = list(MY_LIBRARY.playlists.values())[1]

# Keep Track Artist and Title
tracks = [{'artist': track.artist, 'title': track.title} for track in pl_1.tracks]

# Export with `pandas`
pd.DataFrame(tracks).to_csv("playlist_0.csv")
