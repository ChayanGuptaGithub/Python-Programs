print("enter the number of elements:",end=' ')
n=int(input())
a=[]
for i in range(0,n):
    print("Element at index: ",i)
    ele=int(input(">>"))
    a.append(ele)
print(a)
key=int(input("Enter the element to be searched: "))
for i in range(0,n):
    if(a[i]==key):
        x=1
        break
    else:
        x=0

if(x==1):
    print("Element found at index", i)
else:
    print("Element not found")