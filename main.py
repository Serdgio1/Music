from yandex_music import Client

client = Client('y0_AgAAAABBkqCXAAG8XgAAAAD45Oi9ReP_tAYzT8uWDJ5frBv4-VShbD0')
client.init()

def search(track_name):
    search_result = client.search(track_name)
    if search_result.best:
        type_ = search_result.best.type
        best = search_result.best.result
        if type_ != 'track':
            return None
        else:
            return best
print(search('go robot')['id'])

def track_like(track_name):
    if search(track_name) != None:
        client.users_likes_tracks_add(search(track_name)['id'])
        print("ok")

def track_like(track_name):
    if search(track_name) != None:
        client.users_likes_tracks_remove(search(track_name)['id'])
        print("ok")

def add_playlist(playlist_name):
    client.users_playlists_create(playlist_name)

