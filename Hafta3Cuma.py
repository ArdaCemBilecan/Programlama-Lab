def olasilik(uzay,olay):
    return len(olay)/len(uzay)

def isPrime(sayi):
    if sayi!=1:
        for i in range(2,sayi//2):
            if  sayi%i==0:
                return False
    else:
        return False
    return True

from sympy import FiniteSet

uzay = FiniteSet(*range(1,100))
asalSayilar=[]
for i in uzay:
    if isPrime(i)==True:
        asalSayilar.append(i)

a = olasilik(uzay,asalSayilar)
print(a)

        

