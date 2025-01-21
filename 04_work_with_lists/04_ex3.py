digits = list(range(1, 100)) #1000001
#print 1000000 digits
for i in digits:
    print(i)
#sum , max, min
print(f"\n sum 1000000: {sum(digits)}")
print(f"\n max : {max(digits)}")
print(f"\n min : {min(digits)}")

#odd numbers
print("\nodd numbers\n")
digits2 = list(range(1, 21, 2))
for d in digits2:
    print(d)
print("\n3-31\n")
digits3 = list(range(3, 31, 3))
for d in digits3:
    print(d)

print("\n cube numbers\n")
numbers = [1**3, 2**3, 3**3, 4**3,5**3,6**3,7**3,8**3,9**3,10**3]
for n in numbers:
    print(n)
print("\n list generator cube numbers\n")
numbers1 = [n**3 for n in range(1,11)]
print (numbers1)