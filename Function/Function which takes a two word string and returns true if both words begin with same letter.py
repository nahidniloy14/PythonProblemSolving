def string_check():
    string1 = input("Enter 1st String :")
    string2 = input("Enter 2nd String :")

    split_string1 = string1.split()
    split_string2 = string2.split()

    if split_string1[0].upper() == split_string2[0].upper():
        print("True")
    else:
        print("False")

string_check()
