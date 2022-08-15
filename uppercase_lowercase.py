a=input("Enter any alphabet of any case: ")
a1=ord(a)
if(a1>=65)or(a1<=90):
    print(a,"is in Uppercase")
    print("This is ",a," in Lowercase: ",a.swapcase())

elif(a1>=97)or(a1<=122):
    print(a1,"is in Lowercase")
    print("This is ",a," in Uppercase: ",a.swapcase())

else:
    print("Your character isn't an english alphabet")