def wtf(a, b):
    n_months = 0
    sum_ = 0
    while n_months < 10:
        sum_ += b
        b *= 1.03
        n_months += 1

    return round(sum_ - a * 10)

def wtf1(a, b):
    n_months1 = 0
    sum1_ = 0
    for i in range(10):
        sum1_ += b
        b *= 1.03
        n_months1 += 1
    return round(sum1_ - a * 10)



if __name__ == "__main__":
    print(wtf(8000, 12000))
    print(wtf1(8000, 12000))







