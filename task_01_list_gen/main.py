def main():
    number = int(input('Введите число N: '))
    num_list = []

    for numbers in range(1, number + 1):
        if numbers % 2 > 0:
            num_list.append(numbers)

    print('Список из нечётных чисел от 1 до N:', num_list)
    pass


if __name__ == '__main__':
    main()

