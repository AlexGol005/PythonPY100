def is_sum_di(N):
    digits_list = [int(i) for i in str(N)]
    sum_ = sum(digits_list)
    digits_list2 = [int(j) for j in str(sum_)]
    if len(digits_list2) == 2:
        return 'di'
    else:
        return 'not di'

if __name__ == "__main__":
    print(is_sum_di(111))