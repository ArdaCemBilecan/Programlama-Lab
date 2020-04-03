import sys
outputs=[]
Days=[]
Months=[]
def bubbleSort(list_1):
    for i in range(len(list_1)-1):
        for j in range(len(list_1)-1):
            if list_1[j]>list_1[j+1]:
                temp = list_1[j]
                list_1[j]=list_1[j+1]
                list_1[j+1]=temp

def read_File_And_Separation():
    file =sys.argv[1]
    for i in file:
        outputs.append(int(i.split(";")[3].split("-")[1]))

def myHistogram(outputs):
    Dic=dict()
    for item in outputs:
        if item in Dic:
            Dic[item]=Dic[item]+1
        else:
            Dic[item]=1
    return Dic
   
def appointment(histogram):
    for i in histogram:
        Days.append(histogram[i])
    for i in histogram:
        Months.append(i)

def findAverage(Days,Months):
    total = 0
    totalDays=0
    for i in range(len(Days)):
        total = total+Days[i]*Months[i]
        totalDays=totalDays+Days[i]
    return total/totalDays

def find_Middle_Item(list_1):
    n = len(list_1)
    if n%2==1:
        mid = (n-1)//2
        return list_1[mid]
    else:
        middle_1 = n//2-1
        middle_2=n//2
        avarage = (list_1[middle_1]+list_1[middle_2])/2
        return avarage
        
def writeOutput(average,middle):
    middle = str(middle)
    average = str(average)
    file = sys.argv[2]
    file.write("Average is : ")
    file.write(average)
    file.write("\n")
    file.write("Median is: ")
    file.write(middle)
    file.close()
    
read_File_And_Separation()
histogram = myHistogram(outputs)
print(histogram)
bubbleSort(outputs)
appointment(histogram) 
average = findAverage(Days,Months)
middle=find_Middle_Item(outputs)
writeOutput(average,middle)



