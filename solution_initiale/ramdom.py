import random
def generate_random_tree(size: int):
    for _ in range(size):
        value = random.randint(0, 1000)
        print(value)

generate_random_tree(5)