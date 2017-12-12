
dict ={(1): [0, [1, 2, 3], 1, key, 16]}) # 0 текущее значение интервала- тоже надо прибавить, 1 -список интервалов 2-сколько выпадений уже было 3- номер статистика которого ведется 4- фиг его знает возможно последний интервал


def podchet_interv_odd(slovar):
    obshie = 0
    rezult = 0
    for item in slovar:
        if (slovar[item][3] % 2) != 0:
            if (slovar[item][0]) < 1000:
                for it in slovar[item][1]

                rezult = obshie + slovar[item][0]