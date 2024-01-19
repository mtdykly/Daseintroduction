#插入排序
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex=i-1
        current=arr[i]
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1]=arr[preIndex]
            preIndex -=1
        arr[preIndex+1]=current
    return arr

A=[1,5,6,9,3,4,7,2]
B=insertionSort((A))
print(B)