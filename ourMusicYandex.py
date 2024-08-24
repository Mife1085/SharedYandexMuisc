token_user1 = ""
token_user2 = ""

def MusicList(token):
    from yandex_music import Client
    
    client = Client(token).init()
    
    return client.users_likes_tracks()

data_user1 = MusicList(token_user1) 
data_user2 = MusicList(token_user2)   


MusicList_user1 = []
for i in range(0, len(data_user1)):
    MusicList_user1.append(f"{data_user1[i]["album_id"]}:{data_user1[i]["id"]}")

MusicList_user2 = []
for i in range(0, len(data_user2)):
    MusicList_user2.append(f"{data_user2[i]["album_id"]}:{data_user2[i]["id"]}")

SharedPLaylist = []
if MusicList_user1 < MusicList_user2:
    for tracks_1 in range(0, len(MusicList_user1)):
        for tracks_2 in range(0, len(MusicList_user2)):
            if MusicList_user1[tracks_1] == MusicList_user2[tracks_2]:
                SharedPLaylist.append(MusicList_user1[tracks_1])
else:
    for tracks_2 in range(0, len(MusicList_user2)):
        for tracks_1 in range(0, len(MusicList_user1)):
            if MusicList_user2[tracks_2] == MusicList_user1[tracks_1]:
                SharedPLaylist.append(MusicList_user2[tracks_2])

print(f"Кол-во совпадений: {len(SharedPLaylist)}")
for i in range(0, len(SharedPLaylist)-1):
    print(f"https://music.yandex.ru/album/{SharedPLaylist[i].split(":")[0]}/track/{SharedPLaylist[i].split(":")[1]}")

