import datetime

# Define the year
year = 2023

# Define a dictionary to hold the counts for each day
counts = {}

# Loop through all the days in the year
for month in range(1, 13):
    for day in range(1, 32):
        try:
            date = datetime.date(year, month, day)
            day_of_week = date.strftime("%A")

            if day_of_week not in counts:
                counts[day_of_week] = 0

            counts[day_of_week] += 1

        except ValueError:
            pass

# Print out the counts for each day
for day, count in counts.items():
    print(day, ":", count)
