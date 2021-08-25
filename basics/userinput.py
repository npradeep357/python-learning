def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


#temp = float(input("enter temperature:"))
# print(weather_condition(temp))

print()
print("String formatting")
#user_input = input("enter your name: ")

#message1 = "Hello %s!" % user_input
# message2 will only work with python 3.6 and above
#message2 = f"Hello {user_input}!"

# print(message1)
# print(message2)

name = input("enter your name: ")
surname = input("enter your surname: ")

message1 = "Hello %s %s!" % (name.capitalize(), surname)
# message2 will only work with python 3.6 and above
message2 = f"Hello {name.title()} {surname}!"

print(message1)
print(message2)
