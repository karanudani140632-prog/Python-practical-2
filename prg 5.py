# 5. Write a function inside another function.



def cal(x, y):
   
    def add():
        return x + y
    
    def multi():
        return x * y

    return add(), multi()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition, multiplication = cal(num1, num2)

print("Addition result:", addition)
print("Multiplication result:", multiplication)


