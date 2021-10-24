def find_numbers_between():
    list_ = []
    a = float(input())
    while a != -1:
        if a == 3:
            while a != 13:
                list_.append(a)
                a = float(input())
        else:
            a = float(input())
    return list_[1:(len(list_) + 1)]


if __name__ == "__main__":
    print(find_numbers_between())

