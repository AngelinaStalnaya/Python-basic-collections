def main():
    all_box = int(input('Кол-во контейнеров: '))
    containers_list = []
    for i in range(all_box):
        list = int(input('Введите вес контейнера: '))
        if list > 200:
            print('Вес введен не верно. Попробуйте снова')
            main()
        containers_list.append(list)
    new_box = int(input('Введите вес нового контейнера: '))
    containers_list.append(new_box)
    containers_list.sort(reverse = True)
    print('Место, на которое нужно поставить  новый контейнер: ', containers_list.index(new_box) + 1)
    pass


if __name__ == '__main__':
    main()
