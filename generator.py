import random

small_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
cap_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specials = ["!", "@", "#", "$", "-"]
rare_specials = ["%", "^", "&", "*", "(", ")"]

def password_generator(length):

    password = []

    # Add the common chars
    password.extend(random.choices(small_chars, k=int(length * 0.5)))
    password.extend(random.choices(cap_chars, k=int(length * 0.4)))
    password.extend(random.choices(numbers, k=int(length * 0.3)))

    # Add the common special
    password.extend(random.choices(specials, k=int(length * 0.2)))

    # Add the RAREEEEE!
    password.extend(random.choices(rare_specials, k=int(length * 0.1)))

    random.shuffle(password)

    # Create an empty string and use the .join 
    return "".join(password)

# Usage
password_length = 16
generated_password = password_generator(password_length)
print(f"Generated Password: ",{generated_password})