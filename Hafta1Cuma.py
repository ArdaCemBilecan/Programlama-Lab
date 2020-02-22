#def maxOfTwo(a,b):
#    if a>b:
#        return a
#    else:
#        return b
#
#def maxOfThree(a,b,c):
#    if c > maxOfTwo(a,b):
#        return c
#    else:
#        return maxOfTwo(a,b)
#
#def listeRecursive(liste=[4,-3,5,-2,-1,2,6,-2]):
#    if (len(liste)==0):
#        return 0
#    if (len(liste)==1):
#        return liste[0]
#    n = len(liste)
#    left_i = 0
#    left_j = n//2
#    right_i = (n//2)+1
#    right_j = n
#    leftSum = listeRecursive(liste[0:3])
#    rightSum = listeRecursive(liste[4:8])
#    t,templeLeftSum =0,0
#    for i in range(left_j,left_i,-1):
#        t = t + liste[j]
#        if(t>templeLeftsum):
#            templeLeftSum = t
#        templeRightSum,x=0,0
#        x = x+liste[i]
#        if(t>templeRightSum):
#            templeRightSum = x
#    centerSum = leftSum+rightSum
#    return maxOfThree(leftSum,rightSum,centerSum)
#
#a = listeRecursive(liste = [4,-3,5,-2,-1,2,6,-2])
#print(a)

# Bubble Sort:
l2 = [2,5,3,1,4,6,8,7,0,9]
kontrol = 0
temp = 0
for i in range (10):
    for j in range(9):
        if(l2[j]>l2[j+1]):
            temp = l2[j]
            l2[j]=l2[j+1]
            l2[j+1]=temp
            kontrol = 1
    if(kontrol !=1):
        break
print("BUBLE SORT")
print(l2)

# Selection Sort
# Buradaki amacımız en küçüğü bulup önce 0. indexe atıyoruz
#sonra indexi 1 arttırıp yine en küçüğü bullup 1. indexe atıyoru ve böyle devam ediyor

l2 = [2,5,3,1,4,6,8,7,9,0]
for i in range (10):
   minIndex = i
   for j in range(i+1,10):
       if(l2[j]<l2[minIndex]):
           minIndex = j
   temp = l2[i]
   l2[i]=l2[minIndex]
   l2[minIndex]=temp

print("Selection Sort")
print(l2)
    


            
      

  
        
