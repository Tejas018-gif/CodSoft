#to create a basic calculator
print("Lets calculate!")
result=0
val1=int(input("Enter the 1st value: "))
val2=int(input("Enter the 2nd value: "))
op=input("Enter any one of the operator(+,-,*,/,%): ")
if op=="+":
    result=val1+val2
elif op=="-":
    if val1>=val2:
        result=val1-val2
    else:
        result=-(val2-val1)
elif op=="*":
    result=val1*val2
elif op=="/":
    if val2==0: 
        print("Please enter a value rather than 0")
    else:
        result=val1/val2
elif op=="%":
    result=val1%val2
else:
    print("Please enter any one of the operators(+,-,*,/)")
print("Your answer is : ",result)

