# Write a program which can compute the factorial of a given numbers.The results should be printed 
# in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

import math

my_list = []

def fact(n):
    for i in range(n):
        my_list.append(i)
        return math.factorial(n)
factorial = fact(8)
print(factorial)


    