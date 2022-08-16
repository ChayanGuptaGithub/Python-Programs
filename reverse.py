def reverse(str):
    str = str[::-1]
    return str
s = input("Enter a string ")
print("The original string  is : ", s)
print("The reversed string using extended slice operator  is : ", reverse(s))