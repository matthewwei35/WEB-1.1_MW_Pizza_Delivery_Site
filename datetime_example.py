from datetime import datetime

# Create a datetime object
datetime_obj = datetime.now()

# Convert a datetime object to a string
string_date = datetime_obj.strftime('%m / %d / %Y')
print(string_date)

# Create a new datetime obj via strptime()
another_date = datetime.strptime('02-18-2021', '%m-%d-%Y')
print(another_date)
