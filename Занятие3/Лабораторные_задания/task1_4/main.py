def endless_row_sum(epsilon = 0.0001):
    sum = 0
    n = 1
    term = 1 / 2**n
    while term >= epsilon:
        sum += term
        n += 1
        term = 1 / 2 ** n
    return sum

def aaa(epsilon = 0.0001):
    while True:
        item_n = 1 / 2**2
        if item_n < epsilon:
            break



if __name__ == "__main__":
    print(endless_row_sum(epsilon = 0.0001))
    print(aaa(epsilon = 0.0001))
