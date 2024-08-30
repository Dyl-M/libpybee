# -*- coding: utf-8 -*-

"""File Information
@file_name: Library.py
@author: Dylan "dyl-m" Monfret
Script dedicated to `Library` Object
"""

import plistlib
import unidecode
import urllib.parse as u_parse

from libpybee.Track import Track
from libpybee.Playlist import Playlist


class Library:
    """A class to store MusicBee Library information."""

    def __init__(self, lib_path: str):
        """Initialize a Library object
        @param lib_path: Path to the "iTunes" .xml file for the MB library.
        """
        # Reading XML file
        self.lib_path = lib_path
        with open(self.lib_path, "rb") as lib_file:
            mbl = plistlib.load(lib_file)

        # Basic information about current MusicBee library
        self.major_version = mbl.get('Major Version')
        self.minor_version = mbl.get('Minor Version')
        self.app_version = mbl.get('Application Version')
        self.music_folder = mbl.get('Music Folder').replace('file://localhost/', '')
        self.lib_id = mbl.get('Library Persistent ID')

        # Formatting content into dictionaries and classes: Track & Playlist
        tracks_raw = mbl.get('Tracks')
        playlists_raw = mbl.get('Playlists')
        self.tracks = {}
        self.playlists = {}
        self.playlist_folders = {}
        self.__get_tracks(t_dict=tracks_raw, n_tracks=len(tracks_raw))
        self.__get_playlist(p_list=playlists_raw, n_tracks=len(tracks_raw))

    def __str__(self):
        """Summarize the MusicBee Library Class"""
        return ("- MusicBee Library Information -\n"
                f"* MusicBee Version: {self.app_version}\n"
                f"* Library ID: {self.lib_id}\n"
                f"* Library location: {self.music_folder}iTunes Music Library.xml\n"
                f"* Major Version: {self.major_version}\n"
                f"* Minor Version: {self.minor_version}\n"
                f"* Number of tracks: {len(self.tracks)}\n"
                f"* Number of playlists: {len(self.playlists)}\n"
                f"* Number of playlist folders: {len(self.playlist_folders)}")

    def __get_playlist(self, p_list: list, n_tracks: int):
        """Set each tracks of the MusicBee Library as Track object and store them in `Library.tracks` attribute.
        @param p_list: list of playlists information
        @param n_tracks: number of tracks in the Library for ID formatting.
        """
        for attributes in p_list:
            if attributes.get('Folder'):  # Managing Playlist Folder
                self.playlist_folders[attributes.get('Playlist Persistent ID')] = {
                    'folder_name': attributes.get('Name'),
                    'folder_alternate_id': str(attributes.get('Playlist ID')),
                    'playlists': []}
            else:
                # Init.
                p_id = str(attributes.get('Playlist ID'))
                p = Playlist(p_id)

                # Base
                p.name = attributes.get('Name')

                # Optional
                p.all_items = attributes.get('All Items')
                p.persistent_id = attributes.get('Playlist Persistent ID')
                p.folder_id = attributes.get('Parent Persistent ID')
                p.tracks = [self.tracks[f'{t["Track ID"]:0{len(str(n_tracks))}d}']
                            for t in attributes.get('Playlist Items', [])]

                # Object stored in Library attribute `playlists`
                self.playlists[p_id] = p

                # Object stored in Library attribute `playlist_folders` if included in a folder
                if p.folder_id:
                    self.playlist_folders[p.folder_id]['playlists'].append(p)

    def __get_tracks(self, t_dict: dict, n_tracks: int):
        """Set each tracks of the MusicBee Library as Track object and store them in `Library.tracks` attribute.
        @param t_dict: dictionary of tracks information
        @param n_tracks: number of tracks in the Library for ID formatting.
        """
        for _, attributes in t_dict.items():
            # Init.
            t_id = f'{attributes.get("Track ID"):0{len(str(n_tracks))}d}'
            t = Track(t_id)

            # Base
            t.title = attributes.get('Name')
            t.artist = attributes.get('Artist')

            # Optional
            t.album = attributes.get('Album')
            t.album_artist = attributes.get('Album Artist')
            t.album_rating = int(attributes.get('Album Rating')) if 'Album Rating' in attributes else None
            t.artist_list = self.__multi_tag(attributes, 'Artist')
            t.bitrate = int(attributes.get('Bit Rate'))
            t.bpm = int(attributes.get('BPM')) if 'BPM' in attributes else None
            t.comments = attributes.get('Comments')
            t.compilation = 'Compilation' in attributes
            t.composer = attributes.get('Composer')
            t.date_added = attributes.get('Date Added')
            t.date_modified = attributes.get('Date Modified')
            t.disc_count = int(attributes.get('Disc Count')) if 'Disc Count' in attributes else None
            t.disc_number = int(attributes.get('Disc Number')) if 'Disc Number' in attributes else None
            t.encoder = attributes.get('Encoder')
            t.episode_date = attributes.get('Episode Date')
            t.file_location = u_parse.unquote(u_parse.urlparse(attributes.get('Location')).path)
            t.genre = self.__multi_tag(attributes, 'Genre')
            t.grouping = attributes.get('Grouping').split("; ") if 'Grouping' in attributes else None
            t.kind = attributes.get('Kind')
            t.last_played = attributes.get('Play Date UTC')
            t.length = int(attributes.get('Total Time'))
            t.movement_count = int(attributes.get('Movement Count')) if 'Movement Count' in attributes else None
            t.movement_name = attributes.get('Movement Name')
            t.movement_number = int(attributes.get('Movement Number')) if 'Movement Number' in attributes else None
            t.play_count = int(attributes.get('Play Count')) if 'Play Count' in attributes else 0
            t.persistent_id = attributes.get('Persistent ID')
            t.rating = float(attributes.get('Rating')) if 'Rating' in attributes else None
            t.release_date = attributes.get('Original Year')
            t.sample_rate = attributes.get('Sample Rate')
            t.skip_count = int(attributes.get('Skip Count')) if 'Skip Count' in attributes else 0
            t.skip_date = attributes.get('Skip Date')
            t.track_count = int(attributes.get('Track Count')) if 'Track Count' in attributes else None
            t.track_number = int(attributes.get('Track Number')) if 'Track Number' in attributes else None
            t.track_type = attributes.get('Track Type')
            t.size = int(attributes.get('Size'))
            t.work = attributes.get('Work')
            t.year = attributes.get('Year')

            # Object stored in Library attribute `tracks`
            self.tracks[t_id] = t

    @staticmethod
    def __multi_tag(t_dict: dict, att_name: str):
        """Register multiple value for a same tag (built especially for Genre and Artist tags).
        @param t_dict: dictionary of tracks information
        @param att_name: name of the attribute
        @return: values of the attribute as list or an empty list if no artist are found.
        """
        values_list = set()
        tag_idx = 1

        if f'{att_name}1' in t_dict.keys():
            while f'{att_name}{tag_idx}' in t_dict.keys():
                values_list.add(t_dict.get(f'{att_name}{tag_idx}'))
                tag_idx += 1
            return sorted(list(values_list), key=lambda tag: unidecode.unidecode(tag).lower())

        if f'{att_name}' in t_dict.keys():
            return [t_dict.get(f'{att_name}')]

        return []
