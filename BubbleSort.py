def BubbleSort(alist):
    i=0;
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i]
                alist[i]=alist[i+1]
                alist[i+1]=temp
alist = [4,2,8,5,1,8,0,4,6,33]
BubbleSort(alist)
print(alist)

                            
