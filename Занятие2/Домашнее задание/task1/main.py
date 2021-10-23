if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

    min_value_index = 0
    min_value = list_[0]

    for n, value in enumerate(list_):
        if value <= min_value:
            min_value_index = n
            min_value = list_[n]

    print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
