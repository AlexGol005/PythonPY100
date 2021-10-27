def reverse_most_long_word(str_: str) -> str:
    list_ = str_.split(' ')
    list2_ = []
    list3_ = []
    for i in list_:
        list2_.append(len(i))
    a = list_[list2_.index(max(list2_))]
    for j in list_:
        if len(j) == max(list2_):
            list3_.append(j[::-1])

    return list3_



if __name__ == "__main__":
    print(reverse_most_long_word('am 1 1234   12 12346      12345  22 56789'))
