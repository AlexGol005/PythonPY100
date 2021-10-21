#функция - одинаковые первые символы
def task(str1, str2, k):
    if str1[0] == str2[0] == k:
        answer = 'ДА'
    else:
        answer = 'НЕТ'
    return answer

#функция - первые n символов равны (слишком сложно, см ответ Х))
def is_slice(str1, str2, n):
    i = 1
    while i <= n:
        if str1[0] == str2[0]:
            str1 = str1[1:(len(str1) + 1)]
            str2 = str2[1:(len(str2) + 1)]
            i += 1
            answer = 'ДА'
        else:
            answer = 'НЕТ'
            break
    return answer




if __name__ == "__main__":
    str1 = 'kkky'
    str2 = 'kklo'
    n = 3
    print(is_slice(str1, str2, n))
