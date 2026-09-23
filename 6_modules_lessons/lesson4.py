# date and time module
import datetime

# Current date and time hello!!!!
now = datetime.datetime.now()

print("Current Date and Time:", now)

# Current date
today = datetime.date.today()

print("Date:", today)

# Current time
current_time = datetime.datetime.now().time()

print("Time:", current_time)

# Date components
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Time components
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
