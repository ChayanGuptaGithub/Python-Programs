import math

print("Enter the no. of elements in your list: ",end=' ')
n=int(input())
list=[]
for i in range(0,n):
    print("Element at index",i,"=",end=' ')
    ele=int(input())
    list.append(ele)
print("Enter the element you want to search:",end=' ')
key=int(input())
beg=0
last=n-1
x=0
while(beg<=last):
    mid=(last+beg)//2
    if(list[mid]==key):
        print(key,"found at index",mid)
        x=1
        break
    elif(list[mid]<key):
        last=mid+1
    elif(list[mid]>key):
        beg=mid-1