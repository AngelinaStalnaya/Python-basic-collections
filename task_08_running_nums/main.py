def main():
    step = int(input('Сдвиг: '))
    my_list = [1, 2, 3, 5, 12, 18, -6, 0, -2568, 128]
    new_list = my_list[-step:] + my_list[:-step]
    print('Изначальный список: ', my_list)
    print('Сдвинуй список: ', new_list)
    pass


if __name__ == '__main__':
    main()
