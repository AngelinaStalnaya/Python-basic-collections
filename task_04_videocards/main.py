def main():
    cards = int(input('Кол-во видеокарт: '))
    old_list = []
    for card in range(1, cards + 1):
        print(card, 'Видеокарта: ', end='')
        SNo = int(input())
        old_list.append(SNo)
    new_list = old_list
    all_cards = len(new_list)
    id = max(new_list)
    for i in range(all_cards + 1):
        print(new_list[i])
        if new_list[i] == id:
            new_list.pop(i)

    print('Старый список видеокарт: ', old_list)
    print('Новый список видеокарт: ', new_list)
    pass


if __name__ == '__main__':
    main()
