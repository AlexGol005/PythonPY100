def is_palindrom(N):
    str_ = str(N)
    print(str_)
    if str_ == str_[::-1]:
        return 'YES'
    else:
        return 'NO'



if __name__ == "__main__":
    print(is_palindrom(6556))
