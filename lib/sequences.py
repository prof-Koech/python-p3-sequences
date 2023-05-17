#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0,1]  # Initialize the sequence with the first two Fibonacci numbers
    while len(sequence)< length:
        next_num= sequence[-1]+sequence[-2] # Calculate the next Fibonacci number
        sequence.append(next_num) # Add the next number to the sequence
    print(sequence)
print_fibonacci(9)



def print_fibonacci(length):
    sequence = []
    num1=0
    num2=1

    while len(sequence) < length:
        sequence.append(num1)
        num1, num2 = num2, num1 + num2

    print(sequence)