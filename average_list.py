list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Element(",i,")>>",end=' ')
    ele = int(input())
    list.append(ele)
print(list)
sum=0
for i in range(0, n):
    sum=sum+list[i]
print("SUM of the list is ",sum)
avg=sum/n
print("AVERAGE of the list is ",avg)