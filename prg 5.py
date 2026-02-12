# 5. Write a function inside another function.


def fun1(x, y):
    def fun2(a, b):
        return a + b
    
    result = fun2(x, y)
    return result * 2  


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Final result:", fun1(num1, num2))

