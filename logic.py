'''Assignment 3

Operations and Control Flow
File: logic.py
Ask the user to input hours worked.
Use if/elif/else to classify:
Underworked (<20 hours)
Normal (20–40 hours)
Overtime (>40 hours)
Use a for loop to print all employee names.
Use a while loop to repeatedly ask for a task until the user types ""done"".'''

#user to input hours worked
hours=int(input("hours worked:"))
if hours <20:
    print("Underworked")
elif hours <=40:
    print("Normal")
else:
    print("Overtime") 

#for loop to print all employee name
emp=["a","b","c","d"]
for name in emp:
    print(emp)

#use while loop to repeateadly ask for a task until the user types done
while True:
    task=input("Enter task:")   
    if task == "done":
        break     

