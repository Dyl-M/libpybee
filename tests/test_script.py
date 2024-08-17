import unittest
from libpybee import Library, Playlist, Track, DuplicateTrackError, DuplicatePlaylistError


class TestLibrary(unittest.TestCase):

    def setUp(self):
        # Clear the sets before each test
        Track.all_tracks.clear()
        Playlist.all_playlists.clear()
        # Assuming there's a sample XML file path to test with
        self.library = Library(lib_path="Test Library.xml")

    def test_library_initialization(self):
        # Test that the Library object is initialized properly
        self.assertIsInstance(self.library, Library)

    def test_library_tracks(self):
        Track.all_tracks.clear()
        # Test that the library tracks are properly loaded (mock expected)
        self.assertIsNotNone(self.library.tracks)
        self.assertIsInstance(self.library.tracks, dict)

    def test_library_playlists(self):
        Playlist.all_playlists.clear()
        # Test that the library playlists are properly loaded (mock expected)
        self.assertIsNotNone(self.library.playlists)
        self.assertIsInstance(self.library.playlists, dict)


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        Playlist.all_playlists.clear()  # Clear the set before each test
        self.playlist = Playlist(p_id="12345")

    def test_playlist_initialization(self):
        # Test that the Playlist object is initialized properly
        self.assertIsInstance(self.playlist, Playlist)
        self.assertEqual(self.playlist.id, "12345")

    def test_playlist_duplicate(self):
        # Test that a DuplicateTrackError is raised for duplicate IDs
        with self.assertRaises(DuplicatePlaylistError):
            Playlist(p_id="12345")  # This should raise an error since the ID already exists

    def test_playlist_tracks(self):
        # Assuming Playlist has a method to add tracks, we can test adding and retrieving
        track = Track(t_id="67890")
        self.playlist.tracks = [track]
        self.assertIn(track, self.playlist.tracks)


class TestTrack(unittest.TestCase):

    def setUp(self):
        Track.all_tracks.clear()  # Clear the set before each test
        self.track = Track(t_id="67890")

    def test_track_initialization(self):
        # Test that the Track object is initialized properly
        self.assertIsInstance(self.track, Track)
        self.assertEqual(self.track.id, "67890")

    def test_track_duplicate(self):
        # Test that a DuplicateTrackError is raised for duplicate IDs
        with self.assertRaises(DuplicateTrackError):
            Track(t_id="67890")  # This should raise an error since the ID already exists

    def test_track_attributes(self):
        # Assuming Track has attributes like title, artist (the basic ones).
        self.track.title = "Test Title"
        self.track.artist = "Test Artist"
        self.assertEqual(self.track.title, "Test Title")
        self.assertEqual(self.track.artist, "Test Artist")


if __name__ == '__main__':
    unittest.main()
