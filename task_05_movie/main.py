def main():
    films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
             'Леон', 'Богемская рапсодия', 'Город грехов',
             'Мементо', 'Отступники', 'Деревня']
    my_list= []
    all_films = int(input('Сколько фильмов хотите добавить? '))
    for i in range(all_films):
        title = input('Введите название фильма: ')
        if title in films:
            my_list.append(title)
        else:
            print('Ошибка: фильма', title, ' у нас в списке нет :(')
    print('Ваш список любимых фильмов: ', my_list)
    pass


if __name__ == '__main__':
    main()
