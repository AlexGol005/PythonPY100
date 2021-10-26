def how_many_evens_odds(list_):
    list_even = [i for i in list_ if i % 2 == 0]
    list_odd = [i for i in list_ if i % 2 != 0]
    a = len(list_even)
    b = len(list_odd)
    print(a)
    print(b)
    if a < b:
        answer = 'Больше нечётных'
    elif a > b:
        answer = 'Больше чётных'
    else:
        answer = 'равно'
    return answer



if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9, 5, 5]

    print(how_many_evens_odds(list_))
