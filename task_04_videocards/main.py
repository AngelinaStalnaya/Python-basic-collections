def main():

    cards = int(input('Кол-во видеокарт:'))
    old_list = []
    for card in range(cards):
        print(card + 1, 'Видеокарта:', end='')
        SNO = int(input())
        old_list.append(str(SNO))
    print('Старый список видеокарт: [', " ".join(old_list), ']')
    new_list = old_list
    all_cards = len(new_list)
    idcard = max(new_list)
    num = 0
    for i in new_list:
        if i == idcard:
            new_list.pop(num)
        num +=1
    print('Новый список видеокарт: [', " ".join(new_list), ']')



if __name__ == '__main__':
    main()
