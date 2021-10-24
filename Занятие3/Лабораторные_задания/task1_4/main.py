def endless_row_sum(epsilon = 0.0001):
    sum = 0
    i = 2
    term = 1
    while term >= epsilon:
        term = 1 / i
        sum += term
        i += 1
    return sum


if __name__ == "__main__":
    print(endless_row_sum(epsilon = 0.0001))

