# Токены двух пользователей для получения данных
token_user1 = ""
token_user2 = ""

def MusicList(token):
    """Функция получиние данных о плейлисте Мне нравиться"""
    from yandex_music import Client
    
    client = Client(token).init()
    
    return client.users_likes_tracks()

# Запись данных двух пользователей 
data_user1 = MusicList(token_user1) 
data_user2 = MusicList(token_user2)   


# Создание списков песен виде номер_альбома:номер_трека 
MusicList_user1 = []
for i in range(0, len(data_user1)):
    MusicList_user1.append(f"{data_user1[i]["album_id"]}:{data_user1[i]["id"]}")

MusicList_user2 = []
for i in range(0, len(data_user2)):
    MusicList_user2.append(f"{data_user2[i]["album_id"]}:{data_user2[i]["id"]}")


# Нахождение совподаний и запись в список
SharedPLaylist = []
for tracks_1 in range(0, len(MusicList_user1)):
    for tracks_2 in range(0, len(MusicList_user2)):
        if MusicList_user1[tracks_1] == MusicList_user2[tracks_2]:
            SharedPLaylist.append(MusicList_user1[tracks_1])

# Подготовка результата
tracks_info = client.tracks(SharedPLaylist)
tracks_name = []
for i in range(0, len(SharedPLaylist)-1):
    tracks_name.append(f"{t[i]["artists"][0]["name"]} - {tracks_info[i]["title"]}")

# Отображение результата
print(f"Кол-во совпадений: {len(SharedPLaylist)}")
for i in range(0, len(tracks_name)-1):
    print(i)
