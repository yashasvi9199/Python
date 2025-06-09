import string
import random
import secrets

# TODO Generating just strings in uppercase with number digits
print("".join(random.choices(string.ascii_uppercase + string.digits, k=5)))
print("".join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(5)))


def generate_random_characters(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

print(generate_random_characters(10))



def generate_random_characters(length):
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(length))

print(generate_random_characters(10))