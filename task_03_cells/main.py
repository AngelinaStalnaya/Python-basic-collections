def main():
    ceils = int(input('Кол-во клеток: '))
    wrong_data = []
    for i in range(ceils):
        print('Эффективность ', i + 1, 'клетки: ', end= '')
        kpd = int(input())
        if kpd < i:
            wrong_data.append(kpd)
    print('Неподходящие значения: ', wrong_data)
    pass


if __name__ == '__main__':
    main()
