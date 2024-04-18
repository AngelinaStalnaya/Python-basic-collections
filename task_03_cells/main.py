def main():
    cells_num = int(input('Кол-во клеток: '))
    effic_list = []
    for i_cell in range(cells_num):
        print('Эффективность', i_cell + 1, 'клетки:', end=' ')
        efficiency = int(input())
        effic_list.append(efficiency)

    res = []
    for i_rank in range(cells_num):
        if effic_list[i_rank] < i_rank:
            res.append(str(effic_list[i_rank]))
    print('Неподходящие значения: ' + " ".join(res))


if __name__ == '__main__':
    main()
