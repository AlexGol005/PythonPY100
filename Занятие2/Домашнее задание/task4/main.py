if __name__ == "__main__":
    list_ = list(map(int,input('Введите 10 чисел через пробел ').split()))
    a = list_[0]
    list_[0] = max(list_)
    list2_ = list_[:-1]
    list3_ = list2_.append(a)
    print(list2_)

