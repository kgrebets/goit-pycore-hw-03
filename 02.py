import random
import sys

def get_numbers_ticket(min, max, quantity):
    if (min < 1 
        or max > sys.maxsize 
        or quantity < 1 
        or min > max 
        or quantity > (max - min + 1)):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    return sorted(numbers)

#1 49 6 
numbers = []
while len(numbers) == 0:
    try:
        values = input("Please enter min max and numbers count (space split): ")
        min, max, quantity = map(int, values.split())

        numbers = get_numbers_ticket(min, max, quantity)
        if len(numbers) > 0:
            str_numbers = map(str, numbers)
            print("Your numbers: " + str.join(",", str_numbers))
        else:
            print("Not valid input")
    except Exception as e:
        print(f"An error occurred: {e}")  