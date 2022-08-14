a=int(input("The first number(a)= "))
b=int(input("The second number(b)= "))
c=int(input("The third number(c)= "))

if((a>b) and (a>c)):
    if(b>c):
        print(a,">",b,">",c)
        print("a=",a," is greatest")
    elif(c>b):
        print(a, ">", c, ">", b)
        print("a=", a, " is greatest")
elif((b>a) and (b>c)):
    if(a>c):
        print(b,">",a,">",c)
        print("b=",b," is greatest")
    elif(c>a):
        print(b, ">", c, ">", a)
        print("b=", b, " is greatest")

elif((c>a) and (c>b)):
    if(a>b):
        print(c,">",a,">",b)
        print("c=",c," is greatest")
    elif(b>a):
        print(c, ">", b, ">", a)
        print("c=", c, " is greatest")
