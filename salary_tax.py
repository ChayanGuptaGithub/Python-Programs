salary=float(input("Enter Your Salary: Rs"))

if(salary<250000):
    print("No Tax Payable")
elif(salary>=250000)and(salary<500000):
    print("5% Tax Payable")
    salary=salary-((salary*5)/100)
    print("Salary(After Tax Deduction: Rs",salary)
elif(salary>=500000)and(salary<1000000):
    print("20% Tax Payable")
    salary=salary-((salary*20)/100)
    print("Salary(After Tax Deduction: Rs",salary)
elif(salary>=1000000):
    print("30% Tax Payable")
    salary=salary-((salary*30)/100)
    print("Salary(After Tax Deduction: Rs",salary)