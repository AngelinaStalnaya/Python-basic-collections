def main():
    names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    first_day = []
    boys = len(names_list)
    for i in range(0, boys):
        if i % 2 == 0:
            first_day.append(names_list[i])
    print('Первый день: ', first_day)
    pass


if __name__ == '__main__':
    main()
