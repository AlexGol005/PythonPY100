def digits(N):
    digits_list = [int(i) for i in str(N)]
    sum_ = sum(digits_list)
    sum_even = sum([i for i in digits_list if i % 2 == 0])
    how_many_digits = len(digits_list)
    max_ = max(digits_list)
    min_ = min(digits_list)
    even_place = [i for i in digits_list[1::2]]
    difference = digits_list[0] - digits_list[len(digits_list) - 1]
    min_digit = list.index()
    print(even_place)
    return digits_list, sum_, sum_even, how_many_digits, min_, max_, difference



if __name__ == "__main__":
    print(digits(123456))
