if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    # TODO посчитать через ключи
    sum_ = 0
    for fruit in cart:
        sum_ += cart[fruit]
        print(cart[fruit])  # получаем значение по ключу
    print(sum_)
    # TODO посчитать через метод values
