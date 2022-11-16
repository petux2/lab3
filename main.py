#Никулин Максим 368594

items0 = {"и": (1, 5),
        "н": (1, 15),
        "о": (1, 25),
        "ф": (1, 15),
        "д": (1, 10),
        "п": (2, 15),
        "б": (2, 15),
        "а": (2, 20),
        "к": (2, 20),
        "р": (2, 20),
        "в": (3, 25),
        "т": (3, 20)}

#Разделение предметов по размеру
items = [{}, {}, {}]
for i in items0:
    items[items0[i][0] - 1][i] = items0[i]

#Шаблоны всех возможных положений предметов для 9 ячеек
patterns9 = [[3, 3, 3],
            [3, 3, (2, 1)],
            [3, 3, (1, 1, 1)],
            [3, (2, 1), (2, 1)],
            [3, (2, 1), (1, 1, 1)],
            [3, (1, 1, 1), (1, 1, 1)],
            [(2, 1), (2, 1), (2, 1)],
            [(2, 1), (2, 1), (1, 1, 1)],
            [(2, 1), (1, 1, 1), (1, 1, 1)],
            [(1, 1, 1), (1, 1, 1), (1, 1, 1)]]

#Для 7 ячеек
patterns7 = [[3, 3, 1],
            [3, (2, 1), 1],
            [3, (1, 1, 1), 1],
            [(2, 1), (2, 1), 1],
            [(2, 1), (1, 1, 1), 1],
            [(1, 1, 1), (1, 1, 1), 1]]

def inv_gen(patterns0):
    #Выбор шаблонов, количество предметов в которых подходит количеству предметов из списка
    patterns = []
    for i in patterns0:
        c = [0, 0, 0]
        for j in i:
            if type(j) == int: c[j-1] += 1
            else:
                for k in j:
                    c[k-1] += 1
        for j in range(3):
            if c[j] > len(items[j]):
                break
        else: patterns.append(list(i))

    ss = 15 #Начальная сумма
    for i in items0.values(): ss -= i[1] #Вычитание всех очков заранее

    #Перебор
    count = 0
    for i in patterns:
        ll = [[['ё'], ['ё'], ['ё']]] #Список для хранения всех комбинаций на i шаблон
        #Запись в инвентарь построчно
        for j in range(3):
            a = list([i[j]]) if type(i[j]) is int else list(i[j]) #Размер предметов текущей строки
            k = []
            b = []

            #Запись в k всех возможных комбинаций предметов
            for k1 in items[a[0]-1]:
                if len(a) > 1:
                    for k2 in items[a[1]-1]:
                        if len(a) > 2:
                            for k3 in items[a[2] - 1]:
                                if k1 != k2 and k1 != k3 and k2 != k3: k.append(list([k1, k2, k3]))
                        else:
                            if k1 != k2: k.append(list([k1, k2]))
                else:
                    k.append(list([k1]))

            #Генерация готовой строчки
            for m in range(len(k)):
                if len(k[m]) == 1:
                    k[m] = sorted((f'{k[m][0]} '*a[0]).split(' ')[:a[0]])
                elif len(k[m]) == 2:
                    k[m] = sorted((f'{k[m][0]} ' * a[0] + f'{k[m][1]} ' * a[1]).split(' ')[:3])
                elif len(k[m]) == 3:
                    k[m] = sorted(list(k[m]))

            #Запись в b инвентаря с j+1 готовыми строчками
            for m in range(len(ll)):
                for n in k:
                    c = list(ll[m])

                    #Проверка на повторы
                    for y in c:
                        for u in y:
                            for v in n:
                               if v == u: break
                            else: continue
                            break
                        else: continue
                        break
                    else:
                        c[j] = n
                        if sorted(c) not in b: b.append(list(sorted(c)))

            ll = list(b) #Перезапись ll для следующей итерации

            #Подсчёт очков и вывод
            if j == 2: #Если была запись в последнюю строчку
                for m in b:
                    s = ss
                    for n in m:
                        for l in n:
                            s += 2*(items0[l][1] / items0[l][0])
                    if round(s) > 0:
                        print(m, 'Очки: ', round(s))
                        count += 1
    print('Всего комбинаций: ', count)

inv_gen(patterns9)
inv_gen(patterns7)