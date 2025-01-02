

### **1. Python `datetime`**
The `datetime` module in Python provides classes for manipulating dates and times.

**Importing `datetime`:**
```python
from datetime import datetime, date, time, timedelta
```

---

### **2. Getting `datetime` Information**
You can retrieve the current date and time or extract specific components.

**Code:**
```python
# Get the current datetime
now = datetime.now()

# Extract components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
print("Microsecond:", now.microsecond)
```

**Output Example:**
```
Year: 2025
Month: 1
Day: 2
Hour: 14
Minute: 35
Second: 20
Microsecond: 453212
```

---

### **3. Formatting Date Output Using `strftime`**
The `strftime()` method allows you to format dates and times as strings.

**Code:**
```python
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

# Other formatting examples
print("Month/Day/Year:", now.strftime("%m/%d/%Y"))
print("Weekday (Short):", now.strftime("%a"))
print("Weekday (Full):", now.strftime("%A"))
print("12-Hour Clock with AM/PM:", now.strftime("%I:%M %p"))
```

**Output Example:**
```
Formatted Date: 2025-01-02 14:35:20
Month/Day/Year: 01/02/2025
Weekday (Short): Thu
Weekday (Full): Thursday
12-Hour Clock with AM/PM: 02:35 PM
```

---

### **4. String to Time Using `strptime`**
The `strptime()` method converts a string into a `datetime` object.

**Code:**
```python
date_string = "2025-01-02 14:35:20"
converted_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Converted Datetime: {converted_date}")
```

**Output:**
```
Converted Datetime: 2025-01-02 14:35:20
```

---

### **5. Using `date` from `datetime`**
The `date` class is used to work with dates only (no time information).

**Code:**
```python
# Create a date object
today = date.today()
print("Today's Date:", today)

# Components of date
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
```

**Output:**
```
Today's Date: 2025-01-02
Year: 2025
Month: 1
Day: 2
```

---

### **6. Time Objects to Represent Time**
The `time` class is used to represent time independently of the date.

**Code:**
```python
# Create a time object
time_obj = time(14, 35, 20)  # Hour, Minute, Second
print("Time:", time_obj)

# Components of time
print("Hour:", time_obj.hour)
print("Minute:", time_obj.minute)
print("Second:", time_obj.second)
```

**Output:**
```
Time: 14:35:20
Hour: 14
Minute: 35
Second: 20
```

---

### **7. Difference Between Two Points in Time**
You can calculate the difference between two `datetime` objects.

**Code:**
```python
# Define two datetime objects
start_time = datetime(2025, 1, 1, 0, 0, 0)  # Jan 1, 2025
end_time = datetime(2025, 1, 2, 14, 35, 20)  # Jan 2, 2025 at 2:35 PM

# Calculate difference
time_difference = end_time - start_time
print("Difference:", time_difference)
```

**Output:**
```
Difference: 1 day, 14:35:20
```

---

### **8. Difference Between Two Points in Time Using `timedelta`**
The `timedelta` class represents a duration (difference between two dates/times).

**Code:**
```python
# Create timedelta objects
delta1 = timedelta(days=1, hours=12)  # 1.5 days
delta2 = timedelta(days=2, hours=3)  # 2 days, 3 hours

# Add and subtract timedelta
combined = delta1 + delta2
difference = delta2 - delta1

print("Combined timedelta:", combined)
print("Difference timedelta:", difference)

# Adding timedelta to datetime
future_time = now + delta1
print("Future Time:", future_time)
```

**Output:**
```
Combined timedelta: 3 days, 15:00:00
Difference timedelta: 0 days, 15:00:00
Future Time: 2025-01-03 02:35:20
```

---

### Summary Table

| **Topic**                            | **Key Function/Class** | **Example**                                                |
|--------------------------------------|-------------------------|------------------------------------------------------------|
| Get `datetime` Information           | `datetime.now()`        | Extract year, month, day, hour, minute, etc.              |
| Format Date Output                   | `strftime()`            | Convert `datetime` to a formatted string                  |
| String to Time                       | `strptime()`            | Convert string to `datetime`                              |
| Work with `date`                     | `date.today()`          | Manipulate date-only objects                              |
| Work with `time`                     | `time()`                | Manipulate time-only objects                              |
| Difference Between Two Times         | `datetime` arithmetic   | Subtract two `datetime` objects                           |
| Durations and Arithmetic with Time   | `timedelta`             | Add or subtract durations                                 
