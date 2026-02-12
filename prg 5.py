# 5. Write a function inside another function.


def outer_function(x, y):
    def inner_addition(a, b):
        return a + b
    
    result = inner_addition(x, y)
    return result * 2  


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Final result:", outer_function(num1, num2))
