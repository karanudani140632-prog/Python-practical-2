''' 3. Function to Calculate Factorial (Using Recursion)
 Implement factorial using:
    o Normal function
    o Recursive function '''

def factorial_iterative(n):
    if n < 0:
        return "Error! Factorial of a negative number doesn't exist."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n < 0:
        return "Error! Factorial of a negative number doesn't exist."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


num = int(input("Enter a number: "))

print("Factorial using iterative function:", factorial_iterative(num))
print("Factorial using recursive function:", factorial_recursive(num))
