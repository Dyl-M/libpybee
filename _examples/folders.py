# -*- coding: utf-8 -*-

"""File Information
@file_name: folders.py
@author: Dylan "dyl-m" Monfret
Display Playlists folders and their content
"""

import libpybee

MY_LIB = libpybee.Library('../_tests/test_lib_02.xml')
folders = MY_LIB.playlist_folders

for _, folder in folders.items():
    print(f'FOLDER: {folder["folder_name"]}')

    for playlist in folder['playlists']:
        print(playlist)
