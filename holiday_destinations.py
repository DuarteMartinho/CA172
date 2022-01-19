# Create a list and asign it to a variable
holidays_destinations = ["America", "Dubai", "Paris", "Maldives"]

# Print your list
print(holidays_destinations)

# Remove the destination you least like it
holidays_destinations.pop(2)

# Create a variable and assign it to a new user input
new_holiday = input("Please enter your new destination: ")

# Append your new winter destination
holidays_destinations.append(new_holiday)

# Print in order of preference
print(holidays_destinations[1], "is my favorite destinations.")
print(holidays_destinations[2], "is my second destination.")
print(holidays_destinations[3], "is my third destination.")
print(holidays_destinations[0], "is my fourth destination.")


