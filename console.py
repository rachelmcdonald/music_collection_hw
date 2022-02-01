import pdb 
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository  
import repositories.artist_repository as artist_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist("Slipknot", 9)
artist_repository.save(artist_1)
artist_2 = Artist("Joji", 1)
artist_repository.save(artist_2)

artists = artist_repository.select_all()

album = Album("Volume 3: The Subliminal Verses", artist_1, 2004)
album_repository.save(album)

albums_of_artist_1 = album_repository.albums_for_artist(artist_1)

pdb.set_trace()