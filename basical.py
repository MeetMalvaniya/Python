num1=int( input("Enter First No :"))
num2=int(input ("Enter Secont No :"))
op = input("Enter Operator :")

if op == "+":
    print(num1+num2)

elif op == "-":
    print(num1-num2)

elif op == "*":
    print(num1*num2)

elif op == "/":
    print(num1/num2)

elif op == "%":
    print(num1%num2)

else:
    print("Invalid Operator")