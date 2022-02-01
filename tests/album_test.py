import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    
    def setUp(self):
        self.album = Album("All Hope Is Gone", "Slipknot", "Nu Metal", 2008)