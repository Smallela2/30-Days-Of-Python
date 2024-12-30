import random
import string

def random_user_id():
    # Generate a random string of 6 characters (letters and digits)
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return user_id

print(random_user_id())  # Example output: '1ee33d'


import random
import string

def user_id_gen_by_user():
    # Get inputs for the number of characters and the number of IDs
    num_chars = int(input("Enter the number of characters for each ID: "))
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    # Generate the IDs
    ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
        ids.append(user_id)
    
    # Return the IDs as a list or print them line by line
    return '\n'.join(ids)

# Test the function
print(user_id_gen_by_user())


from random import randint
def rgb_color_gen():
     r = randint(0, 255)
     g = randint(0, 255)
     b = randint(0, 255)
    # Return the formatted RGB string
     return f"rgb({r},{g},{b})"

# Test the function
print(rgb_color_gen())


from random import randint

def list_of_hexa_colors(count):
    colors = []
    for _ in range(count):
        hex_color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
        colors.append(hex_color)
    return colors


def list_of_rgb_colors(count):
    colors = []
    for _ in range(count):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        rgb_color = f"rgb({r},{g},{b})"
        colors.append(rgb_color)
    return colors


def generate_colors(color_type, count):
    if color_type == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type == 'rgb':
        return list_of_rgb_colors(count)
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."

