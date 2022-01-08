cal_to_sec = 24
x = "hours"


def days_to_units(user_date):
    if user_date > 0:
        return f"{user_date} days are {user_date * cal_to_sec} {x}"
    else:
        return "You entered a negative value"


user_input = ""
while user_input != " exit":
    user_input = input("Hey user enter No of day and I will convert into hours !\n")
    user_data = int(user_input)
    my_var = days_to_units(user_data)

print(my_var)

