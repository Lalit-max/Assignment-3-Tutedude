def factorial(n):
    if n < 0:
        return "Factorial not found\nError 404!!!"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
print("Factorial of", n, "is:", factorial(n))
