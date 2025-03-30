import math
num = float(input("Enter a number: "))

if num <= 0:
    print("Logarithm is undefined for non-positive numbers.")
else:
    
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)  
    sine_result = math.sin(num)  
    
    print(f"Square root of {num}: {sqrt_result}")
    print(f"Natural logarithm (ln) of {num}: {log_result}")
    print(f"Sine of {num} (in radians): {sine_result}")
