def make_album(name_artist, name_album):
    full_info_album= {'Artist' : name_artist, 'Album' : name_album}

    return full_info_album

album1 = make_album('Antrax', '666')
album2 = make_album('Slayer', 'Show no mercy')
album3 = make_album('Pantera', 'Vulgar Display of Power')

print(album1)
print(album2)
print(album3)