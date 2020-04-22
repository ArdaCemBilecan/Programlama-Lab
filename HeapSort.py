def deleteHeap(heap):
    if(len(heap)==0):
        return 0
    heap[0],heap[-1]=heap[-1],heap[0]
    heap.pop()
    build_min_heap(heap)
    
def insertHeap(heap,x):
    heap.append(x)
    build_min_heap(heap)

def min_heapify(array,i):
    left = 2*i+1
    right = 2*i+2
    length = len(array)-1
    smallest = i
    if left <=length and array[i]>array[left]:
        smallest = left
    if right <=length and array[smallest]>array[right]:
        smallest = right
    if smallest !=i:
        array[i],array[smallest] =array[smallest], array[i]
        min_heapify(array,smallest)

def build_min_heap(array):
    for i in reversed(range(len(array)//2-1)):
        min_heapify(array,i)

def heapSort(array):
    array = array.copy()
    build_min_heap(array)
    sorted_array=[]
    for i in range(len(array)):
        array[0],array[-1] = array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
        
    return sorted_array

array1 = [8,10,3,4,7,15,1,2,16]
array2=[8,10,3,4,7,15,1,2,16]
insertHeap(array2,17)
deleteHeap(array2)
print(array2)


