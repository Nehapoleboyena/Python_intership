'''
Assignment1
Basic Employee Data (Variables, Data Types)
File: employee_data.py
Create variables for one employee:
employee_id (int)
name (string)
hourly_rate (float)
is_active (boolean)
Print the values and their data types.
Convert hourly_rate to an integer and print the result.'''

employee_id =10
name="Neha"
hourly_rate=16.15
is_active=bool(1)
print(employee_id,type(employee_id))
print(name,type(name))
print(hourly_rate,type(hourly_rate))
print(is_active,type(is_active))

conv_hourly_rate=int(hourly_rate)
print(conv_hourly_rate,type(conv_hourly_rate))

