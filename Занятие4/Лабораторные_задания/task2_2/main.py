def is_digit_in(N):
    digits_list = [int(i) for i in str(N)]
    print(digits_list)
    if (4 in digits_list and 8 in digits_list) or (9 in digits_list):
        return 'in'
    else:
        return 'not in'



if __name__ == "__main__":
    print(is_digit_in(94))
