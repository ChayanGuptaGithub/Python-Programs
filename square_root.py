import math
n=int(input('Enter a number to find square root: '))
if(n<0):
    print("Negative numbers square root not possible")
else:
    sq=math.sqrt(n)
    print("Square root of",n,"is",sq)
