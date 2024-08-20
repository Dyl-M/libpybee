# -*- coding: utf-8 -*-

"""File Information
@file_name: __sandbox.py
@author: Dylan "dyl-m" Monfret
Script dedicated to `Library` Object
"""

import libpybee

XML = "../_tests/test_lib_01.xml"
MY_LIBRARY = libpybee.Library(XML)

print(MY_LIBRARY)

for track in MY_LIBRARY.tracks.values():
    print(track, track.genre)
