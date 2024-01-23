import random

def random(start, end):
    return random.randint(start, end)

random_number = generate_random_number(1, 100)
print(f"{random_number}")
