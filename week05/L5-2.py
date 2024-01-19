import time
import numpy as np
#以选择排序为例
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
A=np.random.randint(15000,size=10000)
end=len(A)-1
temp=[None]*len(A)

start_selectionsort=time.time()
selection_sort(A)
end_selectionsort=time.time()

print("选择排序用时：%.12f秒"%(end_selectionsort-start_selectionsort))