employee = [("Araf", 200), ("Jabir", 400), ("Faruk", 350), ("Jony", 250)]
def employee_check(employee):
    max_salary = 0
    highest_paid_employee = ''

    for name,salary in employee:
        if salary > max_salary:
            max_salary=salary
            highest_paid_employee=name
        else:
            pass
    return max_salary, highest_paid_employee


#print(employee_check(employee))
#Tuple Unpacking
employee_salary,employee_name=(employee_check(employee))
print(employee_name,"is the highest paid employee")
