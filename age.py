name=input("Enter your name: ")
age=int(input("Enter your age: "))
print("Eligibilty to Vote: ",end=' ')
if age<1:
    print("Invalid age")
elif age<18:
    print("Not Elligible, wait for ", 18 - age, " years")
else:
    print("Elligible")
