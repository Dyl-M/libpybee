# -*- coding: utf-8 -*-

"""File Information
@file_name: export_as_json.py
@author: Dylan "dyl-m" Monfret
Example script: Display all library tracks
"""

import json
import libpybee

MY_LIBRARY = libpybee.Library(lib_path="../_tests/test_lib_01.xml")

# List all tracks and playlists, convert each of them to dictionary
exp_dict = {'Tracks': [track.to_dict() for track in MY_LIBRARY.tracks.values()],
            'Playlists': [playlist.to_dict() for playlist in MY_LIBRARY.playlists.values()]}

# Export as JSON
with open('lib.json', 'w', encoding='utf8') as json_file:
    # "default" parameter set to `str` is mandatory to manage complex values (such as 'datetime' values and Track
    # objects in playlists)
    json.dump(exp_dict, json_file, indent=4, default=str)
