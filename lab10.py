import math

def f(x):
    return x**2 + math.log(x) - 4

def f_prime(x):
    return 2*x + 1/x

def newton_method(a, b, epsilon):
    x_n = a
    
    while True:
        x_next = x_n - f(x_n) / f_prime(x_n)
        
        if abs(x_next - x_n) < epsilon:
            return x_next
        
        x_n = x_next

a = 1.0 
b = 2.0  
epsilon = 1e-6 

root = newton_method(a, b, epsilon)
print(f"Tənliyin təqribi kökü: {root}")
