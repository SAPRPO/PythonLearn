def make_album(name_artist, name_album):
    full_info_album= {'Artist' : name_artist, 'Album' : name_album}

    return full_info_album

while True:
    n_art = input('Enter Artist: ')
    if n_art == 'q':
        break
    n_alb = input('Enter Album name: ')
    if n_alb == 'q':
        break
    info_all = make_album(n_art, n_alb)
    print(info_all)
    for art,alb in info_all.items():
        print(f"{art} : {alb}")
