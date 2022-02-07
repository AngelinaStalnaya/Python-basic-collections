def main():
    step = int(input('Сдвиг: '))
    my_list = [1, 2, 3, 4, 5]
    new_list = my_list[-step:] + my_list[:-step]
    print('Сдвинутый список:', new_list)



if __name__ == '__main__':
    main()
