if __name__ == "__main__":

    print([i**2 if i % 2 == 0 else  -i  for i in range(10)])
    list_ = [i ** 2 if i % 2 == 0 else -i for i in range(10)]
    print(list_)


