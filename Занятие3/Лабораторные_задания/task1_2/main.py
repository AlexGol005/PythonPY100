def factorial(n):
    for i in range(1, n):
        i *= i
        i += i
    return i

if __name__ == "__main__":
    print(factorial(1))
