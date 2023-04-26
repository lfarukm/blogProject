import random

list1 = input("kişileri aralarında (,) ile ayrılmış şekilde giriniz : ")
list1 = list1.split(",")
kazananAdet = int(input("kaç adet kazanan olsun : "))
yedekAdet = int(input("kaç adet yedek olsun : "))

kazanan = []
yedek = []

for i in range(kazananAdet):
    randomList = random.choice(list1)
    list1.remove(randomList)
    kazanan.append(randomList)
for j in range(yedekAdet):
    randomList2 = random.choice(list1)
    list1.remove(randomList2)
    yedek.append(randomList2)

print(f"kazananlar : {kazanan} \n yedekler : {yedek}")
