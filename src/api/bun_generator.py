import random

def random_number(upper_limit):
    return random.randint(1, upper_limit)

def build_image_string(bun_number):
    return str('../static/buns/bun') + str(bun_number) + str('.png')

def get_random_bun():
    number = random_number(42)
    image_string = build_image_string(number)
    return image_string
