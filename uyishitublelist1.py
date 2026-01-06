a = int(input("a ni kiriting:"))
b = int(input("b ni kiriting:"))

sonlar = []

for i in range(a,b):
    if i%2==0:
        sonlar.append(i)


print("sonlar=", sonlar)