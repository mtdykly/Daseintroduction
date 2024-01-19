import time

#选择排序
def selection_sort (number_list):
    length=len(number_list)
    if length<=1:
        return number_list
    for i in range(length):
        min_num_index=i
        for j in range(i+1,length):
            if number_list[j]<number_list[min_num_index]:
                min_num_index=j
        number_list[min_num_index],number_list[i]=number_list[i],number_list[min_num_index]
    return number_list

#归并排序
def merge(list,start,mid,end,temp):
    i=start
    j=mid+1
    count=0
    while i<=mid and j<=end:
        if list[i]<list[j]:
            temp[count]=A[i]
            count+=1
            i+=1
        else:
            temp[count]=A[j]
            count+=1
            j+=1
    while i<=mid:
        temp[count]=A[i]
        count+=1
        i+=1
    while j<=end:
        temp[count]=A[j]
        count+=1
        j+=1
    for k in range(count):
        list[start+k]=temp[k]
    return
def merge_sort(number_list,start,end,temp):
    if start>=end:
        return
    mid=int((start+end)/2)
    merge_sort(number_list,start,mid,temp)
    merge_sort(number_list,mid+1,end,temp)
    merge(number_list,start,mid,end,temp)

import numpy as np
A=np.random.randint(15000,size=10000)
B=np.random.randint(15000,size=10000)
end=len(A)-1
temp=[None]*len(A)

start_mergesort=time.time()
merge_sort(A,0,end,temp)
end_mergesort=time.time()

start_selectionsort=time.time()
selection_sort(B)
end_selectionsort=time.time()

print("归并排序用时：%.12f秒"%(end_mergesort-start_mergesort))
print("选择排序用时：%.12f秒"%(end_selectionsort-start_selectionsort))