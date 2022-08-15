print("This is a simple calculator")
print("Enter two numbers")
a=int(input("a: "))
b=int(input("b: "))

print("press 1 to add",a,"and",b)
print("press 2 to subtract",a,"and",b)
print("press 3 to multiply",a,"and",b)
print("press 4 to divide",a,"and",b)

choice=int(input(">>"))
if(choice<1)or(choice>4):
    print("Wrong Choice")

elif(choice==1):
    print(a,"+",b,"=",a+b)
elif(choice==2):
    print(a,"-",b,"=",a-b)
elif (choice == 3):
    print(a, "*", b, "=", a * b)
elif(choice==4):
    print(a,"/",b,"=",a/b)