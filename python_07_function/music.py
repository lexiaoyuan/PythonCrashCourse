def make_album(singer, album, numbers=''):
    albums = {'singer': singer, 'album': album}
    if numbers:
        albums['numbers'] = numbers
    return albums


print(make_album('张靓颖', '终于等到你'))
print(make_album('邓丽君', '我只在乎你', 20))
print(make_album('汪小敏', '笑看风云'))

while True:
    singer = input("请输入歌手：")
    if not singer:
        break
    album = input("请输入专辑：")
    if not album:
        break
    print(make_album(singer, album))
