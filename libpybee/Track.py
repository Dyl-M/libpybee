# -*- coding: utf-8 -*-

"""File Information
@file_name: Track.py
@author: Dylan "dyl-m" Monfret
Script dedicated to `Track` Object
"""


class Track:
    """A class to store track information."""

    all_tracks = set()

    def __init__(self, t_id=str):
        """Initialize a Track object. Attributes are set as None / empty / 0 with direct call to the class.
        @param t_id: Track ID.
        """
        if t_id in Track.all_tracks:
            raise DuplicateTrackError("Track ID already exists in current database.")
        self.id = t_id
        Track.all_tracks.add(self.id)

        self.title = None
        self.artist = None

        self.album = None
        self.album_artist = None
        self.album_rating = None
        self.artist_list = []
        self.bitrate = None
        self.bpm = None
        self.comments = None
        self.compilation = None
        self.composer = None
        self.date_added = None
        self.date_modified = None
        self.disc_count = None
        self.disc_number = None
        self.encoder = None
        self.episode_date = None
        self.file_location = None
        self.genre = []
        self.grouping = []
        self.kind = None
        self.last_played = None
        self.length = None
        self.movement_count = None
        self.movement_name = None
        self.movement_number = None
        self.play_count = 0
        self.persistent_id = None
        self.rating = None
        self.release_date = None
        self.sample_rate = None
        self.skip_count = 0
        self.skip_date = None
        self.track_count = None
        self.track_number = None
        self.track_type = None
        self.size = None
        self.work = None
        self.year = None

    def __iter__(self):
        """Iterate over the attributes"""
        for attr, value in self.__dict__.items():
            yield attr, value

    def __str__(self):
        """Print Track object in the following format: 'Displayed Artist' - 'Track Title'."""
        return f'[{self.id}] {self.artist} - {self.title}'

    def to_dict(self):
        """Get a Track object as a dictionary."""
        return dict(self)


class DuplicateTrackError(Exception):
    """Exception raised when attempting to add a track to the Library with an existing ID."""
