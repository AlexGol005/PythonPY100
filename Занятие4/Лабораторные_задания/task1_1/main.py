def square_generator(n, m):
    return [i ** 2 for i in range(n, m + 1)]


if __name__ == "__main__":
    print(square_generator(1, 3))
