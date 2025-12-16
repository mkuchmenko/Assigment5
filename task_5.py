

employees = [
    {"name": "Олена", "department": "Marketing", "salary": 25000},
    {"name": "Ігор", "department": "IT", "salary": 55000},
    {"name": "Наталія", "department": "Marketing", "salary": 28000},
    {"name": "Олег", "department": "HR", "salary": 22000},
    {"name": "Андрій", "department": "IT", "salary": 48000},
    {"name": "Марія", "department": "IT", "salary": 52000},
]

def  get_department_stats(employee_list, target_dept):
    average_salary = 0
    count = 0
    for worker in employee_list:

        if worker["department"]==target_dept:

            average_salary+=worker["salary"]
            count+=1
            a=worker["salary"]
            top=0
            if a>top:
                top=a
                top_earner=worker["name"]

    print("department:", target_dept)
    print("avarage salary:",average_salary/count)
    print("top earner:", top_earner)
    print("count:",count)

get_department_stats(employees,"IT")
print()
get_department_stats(employees, "Marketing")