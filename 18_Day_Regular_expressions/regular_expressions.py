import re
from collections import Counter

# Paragraph
paragraph = '''
I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities 
to develop an application what else can you love.
'''

# Normalize the text: lowercase and remove punctuation using regex
normalized_text = re.sub(r'[^\w\s]', '', paragraph.lower())

# Split the text into words
words = normalized_text.split()

# Count word occurrences
word_counts = Counter(words)

# Get the most common words
most_common_words = word_counts.most_common()

# Display results
print(most_common_words)


import re

# Extracting points from the text
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
points = list(map(int, re.findall(r'-?\d+', text)))

# Sort the points
sorted_points = sorted(points)

# Calculate the distance between the furthest particles
distance = sorted_points[-1] - sorted_points[0]

print(f"Extracted points: {points}")
print(f"Sorted points: {sorted_points}")
print(f"Distance: {distance}")


import re

def is_valid_variable(name):
    # Regex pattern to match a valid Python variable name
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))   # True


from collections import Counter
import re

# Original text
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. 
;I found tea@ching m%o@re interesting tha@n any other %jo@bs. 
%Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text
def clean_text(text):
    # Remove special characters using regex
    return re.sub(r'[^\w\s]', '', text)

# Count the three most frequent words
def most_frequent_words(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(3)

# Clean and analyze the text
cleaned_text = clean_text(sentence)
frequent_words = most_frequent_words(cleaned_text)

print("Cleaned Text:")
print(cleaned_text)
print("\nThree Most Frequent Words:")
print(frequent_words)
