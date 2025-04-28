
print("WELCOME TO Simple Calculator")
num1 = int(input("enter the first  number:"))
num2 = int(input("enter the second number:"))
print("+"," - "+" % "," / ","//"," *" ,"**")
operation =input("please insert the operation type :")
if operation == "+":
    result = num1 + num2
    print("result : " + str(num1) + operation + str(num2) + '=' + str(result))
elif operation == "-":
    result=num1-num2
    print("result : " + str(num1) + operation + str(num2) + '=' + str(result))
elif operation == "*":
    result=num1*num2
    print("result : " + str(num1) + operation + str(num2) + '=' + str(result))
elif operation == "/":
    result =num1/num2
    print("result : " + str(num1) + operation + str(num2) + '=' + str(result))
elif operation == "//":
    result =num1//num2
    print("result : " + str(num1) + operation + str(num2) + '=' + str(result))
elif operation == "**":
    result =num1**num2
    print("result : " + str(num1) + operation + str(num2) + '=' + str(result))
else:
    print("error")
