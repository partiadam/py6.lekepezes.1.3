'''
1.3 Feladat
Készíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót: 
egy szavakat tartalmazó lista elemeiből generál egy másik listát, amelyben az eredeti szavak csupa nagybetűs formában szerepelnek! 

Csak a 3 betűnél hosszabb szavak kerülnek átalakítva a másik listába!

A program írja ki az eredeti és a generált listát is a képernyőre!

'''

lista = ['alma','kutya','fa']
lista2 = [szo.upper()for szo in lista if len(szo) > 3]
print(lista)
print(lista2)