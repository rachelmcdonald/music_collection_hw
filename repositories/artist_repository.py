from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name, members) VALUES ($s, %s) RETURNING *"
    values = [artist.name, artist.members]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['members'], row['id'] )
        artists.append(artist)
    return artists


def select(id):
    artist: None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['members'], result['id'] )
    return artist


# def delete_all():
#     sql = "DELETE FROM artists"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM artists WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


def update(artist):
    sql = "UPDATE artists SET (name, members) = (%s, %s) WHERE id = %s"
    values = [artist.name, artist.members, artist.id]
    run_sql(sql, values)
