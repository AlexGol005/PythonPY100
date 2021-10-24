def subsecuense_sum():
    sum = 0
    a = float(input())
    while a != 0:
        sum += a
        a = float(input())
    return sum


if __name__ == "__main__":
    print(subsecuense_sum())
