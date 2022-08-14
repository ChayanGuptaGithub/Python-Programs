lst=[]

n=int(input('Enter the number of elements: '))
print("Enter the elements: ")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

print(lst)

max_term=lst[0]

for i in range(1,n):
    if(max_term<lst[i]):
        max_term=lst[i]

print("Max Term is : ",max_term)