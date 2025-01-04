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
