from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(
            row['title'],
            artist,
            row['genre'],
            row['release_date'],
            row['id']
        )
        albums.append(album)
    return albums

def save(album):
    sql = f"""
    INSERT INTO albums
    (title, artist_id, genre, release_date) 
    VALUES
    (%s, %s, %s, %s)
    RETURNING id
    """
    values = [album.title, album.artist.id, album.genre, album.release_date]
    result = run_sql(sql, values)
    album.id = result[0]['id']

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(
            result['title'],
            artist,
            result['genre'],
            result['release_date'],
            result['id']
            )
    return album


# def delete_all():
#     sql = "DELETE FROM albums"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM albums WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


def update(album):
    sql = """
    UPDATE albums
    SET (title, artist_id, genre, release_date)
    = (%s, %s, %s, %s)
    WHERE id = %s
    """
    values = [
        album.title,
        album.user.id,
        album.genre,
        album.release_date
        ]
    run_sql(sql, values)

def albums_for_artist(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(
            row['title'],
            artist,
            row['genre'],
            row['release_date'],
            row['id']
            )
        albums.append(album)

    return albums