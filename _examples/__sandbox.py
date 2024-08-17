# -*- coding: utf-8 -*-

"""File Information
@file_name: __sandbox.py
@author: Dylan "dyl-m" Monfret
Script dedicated to `Library` Object
"""

import libpybee

XML = "../libpybee/tests/Test Library.xml"
MY_LIBRARY = libpybee.Library(XML)

PLAYLISTS = MY_LIBRARY.playlists

test = list(PLAYLISTS.values())[1].tracks

for music in test:
    print(music)
