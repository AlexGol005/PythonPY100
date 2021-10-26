def new_big_list(list_: list) -> list:  # приписана аннотация типа, не отрабатывается интерпретатором,
                                        # но ошибку выдавать не будет, если передать не то
    mean =
    return [item for item in list_ if item > mean]


if __name__ == "__main__":
    print(new_big_list([1, 2, 3, 5]))
