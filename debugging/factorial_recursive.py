#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculate the factorial of a non-negative integer using recursion.
        The factorial of n (written n!) is the product of all positive integers up to n.
        By definition, 0! is equal to 1.
    
    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.
    
    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Compute the factorial of the number provided as a command-line argument
f = factorial(int(sys.argv[1]))
# Print the result
print(f)
