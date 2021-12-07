napok = ["Hétfő","Kedd","Szerda","Csütörtök","Péntek","Szombat","Vasárnap"]
start = int(input("Mikor indul?"))
time = int(input("Hány napig voltál távol? :")) 
a = time % 7

if (start + a ) < 7:
    print("Ezen a napon érkezel meg: ", napok[start + a])
else:
    print("Ezen a napon érkezel meg: ", napok[(start + a) - 7])
