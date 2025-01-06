def count_lines_and_words(file_path):
    """
    Counts the number of lines and words in a given file.

    :param file_path: Path to the file
    :return: Tuple (number of lines, number of words)
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        return num_lines, num_words
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return 0, 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

# Using the function for geometry.py
file_path = 'geometry.py'
lines, words = count_lines_and_words(file_path)
print(f"File: {file_path}")
print(f"Number of Lines: {lines}")
print(f"Number of Words: {words}")

