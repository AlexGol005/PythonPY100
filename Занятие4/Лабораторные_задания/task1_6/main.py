def is_bigger(list_):
    a = list_[0]
    b = len([i for i in list_ if i > a])
    return b



if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(is_bigger(list_))
