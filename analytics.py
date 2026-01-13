'''Assignment-4 Part 4: Functions for Productivity Analysis

File: analytics.py

Function: calculate_pay(hours, rate)

Return total pay.

Function: employee_statistics(hours_list)

Return max, min, and average hours.

Function: search_employee(employees, emp_id)

Return employee details if found, otherwise ""Employee not found"".
'''
'''
#return total pay
def calculate_pay(hours,rate):
    return hours*rate
hours=int(input())
rate=int(input())
print(calculate_pay(hours, rate))   
print(calculate_pay(12,5)) '''


#return max,min,avg hours
def employee_statistics(hours_list):
    max_hours=max(hours_list)
    min_hours=min(hours_list)
    avg_hours=sum(hours_list)/len(hours_list)
    return max_hours,min_hours,avg_hours
hours_list=[40,12,50,60,99]
print(employee_statistics(hours_list))

'''
#return employee details if found else employee not found
def search_employee(employees,emp_id):
    for emp in employees:
        if emp["id"]==emp_id:
            return emp
    return "not found"    
employees=[
    {"id" :101,"name":"Neha"},
    {"id":102,"name":"ram"}
]
print(search_employee(employees,101))
print(search_employee(employees,106))'''