# pow fonksiyonunun recursive hali 

def power(a,b):
    if b ==0:
        return 1
    elif b == 1:
        return a
    else:
        if b%2==0 :
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)*a

print(power(2,5))
print(power(2,4))


# Verilen listede alt kümelerin max olan toplami bulma islemi

liste = [4,-3,5,-2,-1,2,6,-2]
maksimum = 0
for i in range(len(liste)):
    for j in range(i,len(liste)):
        t = 0
        for k in range(i,j):
            t = t+liste[k]
        if maksimum<t:
            maksimum = t
            bas = i
            son = j-1
print("Toplam:",maksimum,"Baslangic index:",bas,"Bitis index:",son)



