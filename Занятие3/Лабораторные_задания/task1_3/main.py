def factorizator(n):
     list_ = []
     i = 2
     while n != 1:
         if n % i == 0:
             n = n // i
             list_.append(i)
         else:
             i += 1
     return list_


if __name__ == "__main__":
    print(factorizator(42))
