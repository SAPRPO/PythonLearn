digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#for i in digits:
#    print(i)
for d in digits:
    if d == 1:
        print(f"{d}st")
    elif d == 2:
        print(f"{d}nd")
    elif d == 3:
        print(f"{d}rd")
    else:
        print(f"{d}th")
