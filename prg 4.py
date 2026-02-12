''' 4. Function with Default Arguments
 Write a function to calculate simple interest.
 Keep rate default as 5%. '''

def simple_interest(principal, time, rate=5):
    interest = (principal * time * rate) / 100
    return interest

p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
r_input = input("Enter rate (press Enter to use default 5%): ")

if r_input.strip() == "":
    result = simple_interest(p, t) 
else:
    result = simple_interest(p, t, float(r_input))

print("Simple Interest:", result)
