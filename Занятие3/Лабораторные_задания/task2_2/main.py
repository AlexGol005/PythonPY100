def is_palindrom(str_):
        if str_ == str_[::-1]:
            return "YES!"
        return "NO!"





if __name__ == "__main__":
    str_ = 'caabaac'
    print(is_palindrom(str_))
