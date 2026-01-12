'''Assignment 2:

Managing Employees and Tasks (Lists, Dictionaries, Sets, Tuples)
File: management.py

2.1 List of Employees
Create a list of employee dictionaries.
Add a new employee to the list.
Remove an employee from the list.
Print the total number of employees.

2.2 Task Dictionary
Create a dictionary where keys are employee IDs and values are lists of assigned tasks.
Add a task to an employee.
Remove a task from an employee.
Print all tasks for all employees.

2.3 Unique Skills Using Sets
Create a set containing all unique employee skills.
Add two new skills to the set.
Print the final set of skills.

2.4 Company Holidays Using Tuples
Create a tuple of company holiday dates.
Attempt to change an element and if it fails, Write a comment explaining it.
'''


'''
#2.1
emp=[{"id":101,"name":"Neha","age": 20},
     {"id":102,"name":"swapna","age":18},
     {"id":103,"name":"sakshi","age":22}]
#add 
emp.append({"id":104,"name":"rahul","age":24})
#remove
emp.remove({"id":101, "name":"Neha", "age":20})
print(len(emp))
print(emp)'''
'''
#2.2
task_dic={
    101:["report","email","verify"],
    102:["code","errors"],
    103:["monitor"]
    }
task_dic[103].append("meeting")
task_dic[101].remove("email")
#print(task2)
for emp,tasks_list in task_dic.items():
    print(f"employee {emp} tasks:")
    for each in tasks_list:
        print("-",each)
'''
'''
#2.3
unique_skills={"python","java","c",".net"}
print(unique_skills)
unique_skills.add("dsa")
unique_skills.add("php")
print(unique_skills)
'''

#2.4
company_holiday_dates=("1-12-2018","14-01,2019","25-06-26")
print(company_holiday_dates)
company_holiday_dates[1]=10
#Tuples are immutable and we can't add,remove or change the elements'''