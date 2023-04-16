def even_checker(num1,num2):
    if num1%2==0 and num2%2==0 and num1>num2:
        return num1
    else:
        return num2
print(even_checker(1,4))
