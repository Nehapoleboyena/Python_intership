def safe_productivity_score(task_completed,hours_worked):
    if hours_worked <= 0:
        return "Invalid hours"
    return task_completed/hours_worked
try :
    task_completed = int(input())
    hours_worked = int(input())
    score=safe_productivity_score(task_completed,hours_worked)
    print(score)
except ValueError:
    print("invalid input")    

