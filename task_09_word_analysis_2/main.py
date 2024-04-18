def main():
    word = list(input('Введите слово: '))
    length = len(word)
    len2 = 0
    for i in range(length):
        if word[i] == word[-1-i]:
            len2 += 1
    if length == len2:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')



if __name__ == '__main__':
    main()
