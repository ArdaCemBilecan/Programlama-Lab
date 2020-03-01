#SORTING CODE'S

#Bubble Sort:
liste = [2,5,3,1,4,6,8,7,0,9]
kontrol = 0
temp = 0
for i in range (10):
    for j in range(9):
        if(liste[j]>liste[j+1]):
            temp = liste[j]
            liste[j]=liste[j+1]
            liste[j+1]=temp
            kontrol = 1
    if(kontrol !=1):
        break
print(liste)

#SHELL SORT
def shellSort(liste, n):
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = liste[i]
            j = i
            while j >= gap and liste[j - gap] > temp:
                liste[j] = liste[j - gap]
                j -= gap

            liste[j] = temp
        gap //= 2

liste = [2,5,3,1,4,6,8,7,0,9]
shellSort(liste,len(liste))
print(liste)

#Insertion Sort

def insertionSort(liste):
    n = len(liste)
    for i in range(1,n):
        temp = liste[i]
        j = i-1
        while j>=0 and temp<liste[j]:
            liste[j+1]=liste[j]
            j=j-1
        liste[j+1]=temp
liste = [2,5,3,1,4,6,8,7,0,9]
insertionSort(liste)
print(liste)


