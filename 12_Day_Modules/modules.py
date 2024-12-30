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


