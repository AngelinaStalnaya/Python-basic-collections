def main():
    amount = int(input('Введите кол-во чисел: '))
    num_list = []
    for num in range(amount):
        numbers = int(input('Введите число: '))
        num_list.append(numbers)
    print('Изначальный список: ', num_list)
    num_list.sort()
    print('Отсортированный список', num_list)
    pass


if __name__ == '__main__':
    main()
