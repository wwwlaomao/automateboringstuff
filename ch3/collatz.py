#!/usr/bin/env python3

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number

while True:
    try:
        number = int(input('Please type an integer (2 to exit): '))
        if collatz(number) == 1:
            print('Bye')
            break
    except ValueError:
        pass
