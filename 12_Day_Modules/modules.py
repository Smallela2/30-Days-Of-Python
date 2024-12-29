import random
import string

def random_user_id():
    # Generate a random string of 6 characters (letters and digits)
    user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return user_id

print(random_user_id())  # Example output: '1ee33d'

