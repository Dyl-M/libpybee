# -*- coding: utf-8 -*-

"""File Information
@file_name: Library.py
@author: Dylan "dyl-m" Monfret
Script dedicated to `Library` Object
"""


class Playlist:
    """A class to store playlist information."""

    all_playlists = set()

    def __init__(self, p_id: str):
        """Initialize a Playlist object. Attributes are set as None / empty / 0 with direct call to the class
        @param p_id: Playlist ID.
        """
        if p_id in Playlist.all_playlists:
            raise DuplicatePlaylistError("Playlist ID already exists in current database.")

        else:
            self.id = p_id
            Playlist.all_playlists.add(self.id)

        self.name = None
        self.all_items = None
        self.persistent_id = None
        self.tracks = []
        self.n_tracks = 0

    def __iter__(self):
        """Iterate over the attributes"""
        for attr, value in self.__dict__.items():
            yield attr, value

    def __str__(self):
        """Print Playlist object in the following format: ['ID'] 'Name': 'Number of tracks in the playlist'."""
        return f'[{self.id}] {self.name}: {self.n_tracks} track(s).'

    def to_dict(self):
        """Get a Playlist object as a dictionary."""
        return {key: value for (key, value) in self}


class DuplicatePlaylistError(Exception):
    """Exception raised when attempting to add a duplicate element to a set."""
    pass
