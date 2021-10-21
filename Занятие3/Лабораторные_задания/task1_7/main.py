def how_month(A, B, S):
    month_numer = 0
    while S > 0:
        S = S - B + A
        B *= 1.05
        month_numer += 1
    return month_numer

if __name__ == "__main__":
    print(how_month(8000, 12000, 200000))
