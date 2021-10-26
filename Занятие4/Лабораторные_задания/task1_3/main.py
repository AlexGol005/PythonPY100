def how_many_evens(list_):
    list2_ = []
    return len([i for i in list_ if i % 2 == 0])


if __name__ == "__main__":
    print(how_many_evens([2]))