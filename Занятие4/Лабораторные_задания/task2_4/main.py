def is_sum_di(N):
    digits_list = [int(i) for i in str(N)]
    sum_ = sum(digits_list)

    if sum_ % 7 == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == "__main__":
    print(is_sum_di(4810))
