'''Assignment 5:

Part 1: Exception Handling

File: exceptions.py

Ask the user for hours worked and handle if input is invalid.

Create safe_productivity_score(tasks_completed, hours_worked) function:

Score = tasks_completed / hours_worked

Return an appropriate message when an error occurs. Part 2: Git Workflow

Initialize a Git repository using git init.

Add all project files to the repository.

Create at least three commits:

Commit 1: basic employee data

Commit 2: employee and task management

Commit 3: analytics and exception handling
'''

def safe_productivity_score(task_completed,hours_worked):
    if hours_worked <= 0: # i have used if conditional statement to handle 0 working hours
        return "Invalid hours"
    return task_completed/hours_worked
try :
    task_completed = int(input())
    hours_worked = int(input())
    score=safe_productivity_score(task_completed,hours_worked)
    print(score)
except ValueError:
    print("invalid input")    

def safe_productivity_score(task_completed,hours_worked):
    try: #here i have used ZeroDivisionError
        score = task_completed/hours_worked
        return score
    except ZeroDivisionError:
        return"Invalid hours"
try :
    task_completed = int(input())
    hours_worked = int(input())
    score=safe_productivity_score(task_completed,hours_worked)
    print(score)
except ValueError:
    print("invalid input")   
