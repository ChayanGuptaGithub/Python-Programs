a=int(input('Enter first number'))
b=int(input('Enter second number'))

def gcd(s,b):
    for i in range(1,s+1):
        if(s%i==0)and(b%i==0):
            gcd=i

    return gcd

if a > b:
        small = b
        big=a
else:
    small = a
    big = b

print("GCD of ",a,"and",b,"is",gcd(small,big))