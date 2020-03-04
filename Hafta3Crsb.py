# Dizideki hangi elemandan kaçar tane olduğunu bulan fonksiyon
def myHistogram(liste_1,myDic):
    for i in liste_1:
        if i in myDic:
            myDic[i] = myDic[i]+1
        else:
            myDic[i] = 1
    return myDic

# Verilen degeri kadar tekrar eden deger var mı?   
def repetition(myDic,value):
    for i in myDic:
        if myDic[i]==value:
            return i
    return -1

myDic = dict()
liste_1 = [1,2,2,3,3,3,4,4,4,4]
print(myHistogram(liste_1,myDic))
print("3u arattık: ",repetition(myDic,3))
print("Olmayan Deger Girdik: ",repetition(myDic,5))

#Fibonacci recursive
# 1,1,2,3,5,8,13,21,34.....
def fibo(n):
    #Bu fonksiyon çok fazla tekrar yaptırıyor bu yüzden fazla tercih edilmez
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
def fibo1(n):
    # Bilenen değerleri kümeye atıyoruz böylelikle sürekli n-1 ve n-2 yi hesaplamak
    # zorunda kalmıyoruz daha az işlem yapıyoruz
    known = {0:0,1:1}
    if n in known:
        return known[n]
    else:
        result = fibo1(n-1)+fibo1(n-2)
        known[n] = result
        return result
print(fibo1(6))
print("***************************************")   
# küme oluşturma
from sympy import FiniteSet
from fractions import Fraction
s = FiniteSet(1,1.5,Fraction(1.5),Fraction(2.5),3.5)
for member in s:
    print(member)

t = FiniteSet(1,Fraction(4.5),4.5,6)
if s==t:
    print("True")
else:
    print("FALSE")
#s.intersect(t) kesişimlerini alır
#s.union(t)  birleşimlerini alır
print("***************************************")   
liste_2 = [1,4,7,84,3,6,2,62]
my_d = dict()
my_d = {1:'Bir',2:2,'3':'Three'}

for key in my_d.keys():
    print(key,my_d[key])
if -10 not in my_d:   # -10 adlı bir key yoksa 
    my_d[-10] = 50    # -10 aldı key'e 50yi ata
print("***************************************")  
def my_h(liste_2):
    my_d = {}
    if i not in my_d:
        my_d[i] = 1
    else:
        my_d[i] = i+1
    return my_d

liste_2 = [1,4,7,84,3,6,2,62]
print(my_h(liste_2))

