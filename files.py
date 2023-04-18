'''составить программу которая подсчитывает средний балл студента
иванов и.и 3,9
'''
with open('input_data.txt', encoding='utf8') as f:
    for line in f:
        #print(line,end='')
        fio_lst = line.split()
        #print(fio_lst)
        fio = fio_lst[0] + ' ' + fio_lst[1][0] + '.' + fio_lst[2][0]
        #print(fio)
        ball_lst = fio_lst[3].split(',')
        #print(ball_lst)
        s = 0#summa
        for i in ball_lst:
            s += int(i)
        ball_avg = s / len(ball_lst)
        print(f'{fio} {ball_avg:.2f}')

















