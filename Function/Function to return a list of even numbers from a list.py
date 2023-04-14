def even_number(number_list):
    number=[]
    for i in number_list:
        if i%2==0:
           number.append(i)
        else:
            pass
    return number
print(even_number([12,16,77]))

