# to find the builtin methods
# dir(__builtins__)
day_hours = 24
week_days = 7

week_hours = week_days * day_hours
print(week_hours)

print()
print("trying '+' operator")
x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)

print()
print("trying max()")
student_grades = [9.1, 8.8, 7.5]
max_value = max(student_grades)
print(max_value)

print()
print("trying list.count() to check how many times 10.0 is present in the list")
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))

print()
print("trying str.lower()")
username = "Python3"
print(username.lower())

print()
print("Creating a sample dictionary")
day_temperatures = {'morning': 21.4, 'noon': 34.72, 'evening': 17.3}
print(day_temperatures)
print(type(day_temperatures))

print()
print("Creating a sample tuple")
color_codes = ((1, 2), (3, 4), (5, 6))
print(color_codes)
print(type(color_codes))
