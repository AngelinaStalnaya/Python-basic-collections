def main():
    word = input(('Введите слово: '))
    word = list(word)
    original = 0
    letters = len(word)
    for i in word:
        word.count(i)
        if word.count(i) == 1:
            original += 1
    print('Количество уникальных букв в слове: ', original)
    pass


if __name__ == '__main__':
    main()



# Введите слово: привет
# Кол-во уникальных букв: 6
# Пример 2:
# Введите слово: лава
# Кол-во уникальных букв: 2