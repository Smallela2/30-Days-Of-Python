
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Now: {now}")

# Components
print(f"Day: {now.day}, Month: {now.month}, Year: {now.year}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Timestamp: {now.timestamp()}")

# Format the current date
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Convert string to datetime
date_string = "5 December, 2019"
formatted_time = datetime.strptime(date_string, "%d %B, %Y")
print(f"Converted Datetime: {formatted_time}")

# Time until New Year
new_year = datetime(now.year + 1, 1, 1)
time_until_new_year = new_year - now
print(f"Time until New Year: {time_until_new_year}")

# Time since 1 January 1970
epoch_start = datetime(1970, 1, 1)
time_since_epoch = now - epoch_start
print(f"Time since 1 January 1970: {time_since_epoch}")
