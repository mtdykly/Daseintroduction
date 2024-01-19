#希尔排序
def shell_sort(arr):
    #假设以列表长度1/4作为初始分组距离
    interval=int(len(arr)/4)
    while interval>0:
        for i in range(interval,len(arr)):
            cur_index=i-interval
            while cur_index>=0 and arr[cur_index]>arr[cur_index+interval]:
                arr[cur_index+interval],arr[cur_index]=arr[cur_index],arr[cur_index+interval]
                cur_index-=interval
        interval=int(interval/4)
    return arr

A=[2,3,5,9,7,1,0,6,4]
B=shell_sort(A)
print(B)
