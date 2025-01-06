

## **1. Opening Files for Reading**

To read a file, you use the `open()` function in Python. The syntax is:

```python
file = open(filename, mode)
```

- `filename`: Name of the file you want to open.
- `mode`: The mode in which you open the file. For reading, use `'r'`.

### Example:
```python
# Create a text file with sample content
with open('sample.txt', 'w') as f:
    f.write("Hello, World!\nPython is fun!")

# Open and read the file
file = open('sample.txt', 'r')  # 'r' is for reading
content = file.read()
print(content)  # Outputs the content of the file
file.close()  # Always close the file after use
```

---

## **2. Opening Files for Writing and Updating**

### **Writing (`'w'`)**:
Opens a file for writing. If the file exists, it overwrites the content; if it doesn't, it creates a new file.

### Example:
```python
file = open('write_example.txt', 'w')
file.write("This is a new file.\nWriting some text into it.")
file.close()

# Reading the written file
with open('write_example.txt', 'r') as f:
    print(f.read())
```

### **Appending (`'a'`)**:
Adds content to the end of the file without overwriting.

### Example:
```python
file = open('write_example.txt', 'a')
file.write("\nAdding more lines.")
file.close()

with open('write_example.txt', 'r') as f:
    print(f.read())
```

### **Updating (`'r+'`)**:
Allows reading and writing at the same time.

### Example:
```python
file = open('write_example.txt', 'r+')
file.write("Updated content at the beginning.\n")
file.seek(0)  # Go back to the start of the file
print(file.read())  # Read updated file
file.close()
```

---

## **3. Deleting Files**

You can delete files using the `os` module.

### Example:
```python
import os

# Delete a file
os.remove('write_example.txt')

# Check if file exists before deleting
if os.path.exists('write_example.txt'):
    os.remove('write_example.txt')
else:
    print("File does not exist.")
```

---

## **4. File Types**

### **Text Files (`.txt`)**

Plain text files contain simple text.

### Example:
```python
with open('example.txt', 'w') as f:
    f.write("This is a plain text file.")

with open('example.txt', 'r') as f:
    print(f.read())
```

---

### **JSON Files (`.json`)**

JSON (JavaScript Object Notation) is a lightweight format for data exchange.

#### **Changing JSON to Dictionary**:
```python
import json

# Sample JSON string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
data = json.loads(json_data)
print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

#### **Changing Dictionary to JSON**:
```python
# Convert Python dictionary to JSON string
dict_data = {"name": "Alice", "age": 25, "city": "London"}
json_string = json.dumps(dict_data, indent=4)
print(json_string)
```

#### **Saving as JSON File**:
```python
# Save dictionary as JSON file
with open('data.json', 'w') as f:
    json.dump(dict_data, f, indent=4)
```

---

### **CSV Files (`.csv`)**

CSV (Comma-Separated Values) files store tabular data.

#### **Writing CSV**:
```python
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "London"],
    ["Bob", 30, "Paris"],
]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

#### **Reading CSV**:
```python
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

### **Excel Files (`.xlsx`)**

For handling Excel files, use the `openpyxl` library.

#### **Writing to Excel**:
```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

# Add data
ws.append(["Name", "Age", "City"])
ws.append(["Alice", 25, "London"])
ws.append(["Bob", 30, "Paris"])

# Save the file
wb.save("data.xlsx")
```

#### **Reading from Excel**:
```python
from openpyxl import load_workbook

wb = load_workbook("data.xlsx")
ws = wb.active

for row in ws.iter_rows(values_only=True):
    print(row)
```

---

### **XML Files (`.xml`)**

For handling XML files, use the `xml.etree.ElementTree` module.

#### **Parsing XML**:
```python
import xml.etree.ElementTree as ET

# Sample XML data
xml_data = """<data>
    <person>
        <name>John</name>
        <age>30</age>
    </person>
    <person>
        <name>Alice</name>
        <age>25</age>
    </person>
</data>"""

# Parse XML
root = ET.fromstring(xml_data)
for person in root.findall('person'):
    name = person.find('name').text
    age = person.find('age').text
    print(f"Name: {name}, Age: {age}")
```

---

### Key Points to Remember:
1. **Always close files**: Use `file.close()` or a `with` statement.
2. **Modes**:
   - `'r'`: Read.
   - `'w'`: Write (overwrites).
   - `'a'`: Append.
   - `'r+'`: Read and write.
3. **File paths**:
   - Use relative paths (`data/file.txt`) or absolute paths (`C:/data/file.txt`).
4. **Error handling**:
   - Always check if the file exists before reading or deleting.

