import random

def random_number(number_of_buns):
    print random.random(1, number_of_buns)

def main(number_of_buns):
    random_number(number_of_buns)

if __name__ == '__main__':
    main()
