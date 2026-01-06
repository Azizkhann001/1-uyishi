list1=[1,2,3,4]
soz=input("sozni kiriting:")

yangi=[]
for i in range(len(list1)):
    yangi.append(soz+str(list1[i]))
               
print(yangi)