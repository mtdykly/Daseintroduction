#节点
class Listnode(object):
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

#链表
class List(object):
    def __init__(self):
        self.head=None
    def create(self,alldata):#创建链表，alldata是一组表示对象
        self.head=Listnode(alldata[0])
        cur=self.head
        for i in alldata[1:]:
            p=Listnode(i)
            cur.next=p
            cur=p
        return self.head

    #打印元素
    def print(self):
        if self.head:
            p=self.head
            while p:
                print(p.data,end=' ')
                p=p.next
            print(' ')
        else:
            return

    #增
    def insert(self,value,n):
        q=Listnode(value)#创建一个结点
        if n==0:#判断是否插入作为第一个结点
            q.next=self.head
            self.head=q
        else:
            p=self.head
            count=1
            while count<n:
                p=p.next
                count+=1
            q.next=p.next
            p.next=q
            print("插入成功")
        return

    #删
    def remove(self,value):
        if self.head:
            p=self.head
            while p:
                if p.next.data==value:
                    p.next=p.next.next
                    print("删除成功")
                    break
                else:
                    p=p.next
            if p==None:
                print("删除失败")
        else:
            return None

    #查
    def search(self,value):
        if self.head:
            count=1
            p=self.head
            while p:
                if p.data==value:
                    print("在第%d个结点"%count)
                    break
                else:
                    p=p.next
                    count+=1
            if p==None:
                print("不存在")
        else:
            return None

    #改
    def updata(self,value,n):
        if self.head:
            p=self.head
            count=1
            while count<n:
                p=p.next
                count+=1
            p.data=value
            print("修改成功")
        else:
            return None

list=List()
list.create([x for x in range(10)])
list.print()
list.insert(99,3)
list.print()
list.remove(5)
list.print()
list.search(6)
list.search(86)
list.updata('new',10)
list.print()
