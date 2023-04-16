def even_string_checker(my_string):
    if len(my_string)%2==0:
        return my_string
    else:
        return my_string[0]

names=['Abbas',"Bablu","Camila","Dider"]

print(list(map(even_string_checker,names)))

