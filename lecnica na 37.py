import random
def lecnica():
    dobavka = 0
    stavka = 0.01
    postavleno = 0
    pribyl = 0
    i = 0
    for i in range(1,129):
        # postavleno = postavleno+stavka
        if i > 0 and i < 36:
            # dobavka = dobavka + 0.01
            print('dobavka: ', dobavka)
            postavleno = postavleno + stavka
            pribyl = (stavka) * 36
        if i > 35 and i < 54:
            dobavka =  0.01
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 53 and i < 66:
            dobavka =  0.02
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36

        if i > 65 and i < 75:
            dobavka =  0.03
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 74 and i < 82:
            dobavka =  0.04
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 81 and i < 88:
            dobavka =  0.05
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 87 and i < 93:
            dobavka =  0.06
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 92 and i < 97:
            dobavka =  0.07
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36


        if i > 96 and i < 101:
            dobavka =  0.08
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 100 and i < 105:
            dobavka = 0.09
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 104 and i < 108:
            dobavka = 0.1
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 107 and i < 111:
            dobavka = 0.11
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 110 and i < 114:
            dobavka = 0.12
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 113 and i < 116:
            dobavka = 0.13
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 115 and i < 119:
            dobavka = 0.14
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36

        if i > 118 and i < 121:
            dobavka = 0.15
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36

        if i > 120 and i < 123:
            dobavka = 0.16
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 122 and i < 125:
            dobavka = 0.17
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 124 and i < 127:
            dobavka = 0.18
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 126 and i < 129:
            dobavka = 0.19
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36


        # if i > 107 and i < 112:
        #     dobavka = 0.11
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # if i > 107 and i < 112:
        #     dobavka = 0.11
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        stavka2 = stavka + dobavka
        print('stavka', stavka + dobavka)

        print('shag:', i, ' kolichestvo postavlennogo:', postavleno, '  kompensacija: ', pribyl, 'raznica: ',
              round(pribyl - postavleno, 2))
list_of_steps=[]
def vyigrysh(steps, key, winer, razreshenie):
    dobavka = 0
    stavka = 0.01
    postavleno = 0
    pribyl = 0
    list =[pribyl,razreshenie]
    promegutok = steps - winer[1]
    i = promegutok
    print('key: ',key, 'winer[0]', winer[0] )
    if key == winer[0]:
        # postavleno = postavleno+stavka
        if i > 0 and i < 36:
            # dobavka = dobavka + 0.01
            # print('dobavka: ', dobavka)
            postavleno = postavleno + stavka
            pribyl = (stavka) * 36

            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 35 and i < 54:
            dobavka =  0.01
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 53 and i < 66:
            dobavka =  0.02
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 65 and i < 75:
            dobavka =  0.03
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 74 and i < 82:
            dobavka =  0.04
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 81 and i < 88:
            dobavka =  0.05
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 87 and i < 93:
            dobavka =  0.06
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 92 and i < 97:
            dobavka =  0.07
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 96 and i < 101:
            dobavka =  0.08
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 100 and i < 105:
            dobavka = 0.09
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 104 and i < 108:
            dobavka = 0.1
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 107 and i < 111:
            dobavka = 0.11
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 110 and i < 114:
            dobavka = 0.12
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 113 and i < 116:
            dobavka = 0.13
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)

        if i > 115 and i < 119:
            dobavka = 0.14
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 118 and i < 121:
            dobavka = 0.15
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 120 and i < 123:
            dobavka = 0.16
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 122 and i < 125:
            dobavka = 0.17
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 124 and i < 127:
            dobavka = 0.18
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 126 and i < 129:
            dobavka = 0.19
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
            print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i>128:
            pribyl =-2.49
            print(' AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA na shage igry: ', promegutok)
        list[1] = 1
        list_of_steps.append(promegutok)
    else:
        if i > 0 and i < 36:
            # dobavka = dobavka + 0.01
            # print('dobavka: ', dobavka)
            postavleno = postavleno + stavka
            pribyl = -stavka

        if i > 35 and i < 54:
            dobavka = 0.01
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 53 and i < 66:
            dobavka = 0.02
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1

        if i > 65 and i < 75:
            dobavka = 0.03
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 74 and i < 82:
            dobavka = 0.04
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 81 and i < 88:
            dobavka = 0.05
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
            # print('winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 87 and i < 93:
            dobavka = 0.06
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
            # print('                               winner: ', winer[0], 'na shage igry: ', promegutok)
        if i > 92 and i < 97:
            dobavka = 0.07
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1

        if i > 96 and i < 101:
            dobavka = 0.08
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 100 and i < 105:
            dobavka = 0.09
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 104 and i < 108:
            dobavka = 0.1
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 107 and i < 111:
            dobavka = 0.11
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 110 and i < 114:
            dobavka = 0.12
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 113 and i < 116:
            dobavka = 0.13
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 115 and i < 119:
            dobavka = 0.14
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1

        if i > 118 and i < 121:
            dobavka = 0.15
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1

        if i > 120 and i < 123:
            dobavka = 0.16
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 122 and i < 125:
            dobavka = 0.17
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 124 and i < 127:
            dobavka = 0.18
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1
        if i > 126 and i < 129:
            dobavka = 0.19
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * -1

        list[1] = 0
    if steps ==1: list[1] = 1




    list[0] = pribyl

    return list
        # if i > 107 and i < 112:
        #     dobavka = 0.11
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # if i > 107 and i < 112:
        #     dobavka = 0.11
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # stavka2 = stavka + dobavka
        # print('stavka', stavka + dobavka)
        #
        # print('shag:', i, ' kolichestvo postavlennogo:', postavleno, '  kompensacija: ', pribyl, 'raznica: ',
        #       round(pribyl - postavleno, 2))

globall =0
i =0

for i in range(222,872): #while (ik < 1):
    # ik = ik + 1
    # file_obj = open('100_xodov.txt', 'w')
    # file_obj.close()
    # file_obj = open('100_xodov.txt', 'a')
    # for i in range(600):
    #     chislo = random.randint(0, 36)  # генерируем число
    #     file_obj.write(str(chislo) + '\n')
    #
    # file_obj.close()
    # naime_file = '100_xodov.txt'
    naime_file = str(i) + 'cikl_och.txt'
    print('file: ', naime_file)

    winer = 99
    winner_list =[99,99]

    viborka = []
    file_obj = open(naime_file)
    data_list = file_obj.readlines()
    for line in data_list:
        viborka.append(int(line))
    key = 0
    steps_sesia = 1
    key1 = key
    steps = 0
    razreshenie = 99
    rezult=[0,0]
    summa =0

    while (steps < len(viborka)):

        key = viborka[steps]
        steps = steps + 1
        rezult =  vyigrysh(steps, key, winner_list, razreshenie)
        summa = summa+rezult[0]
        rezult[0] = 0
        razreshenie = rezult[1]
        if razreshenie ==99 or razreshenie ==1:
            if steps > 380:
                print(' ------------------------------------file:',naime_file, '---- выход на шаге: ', steps)
                break
            winner_list[0]=random.randint(0, 36)
            #print('winer:', winner_list[0])
            winner_list[1] = steps
            razreshenie =0
            print('naznachaetsja winer:', winner_list[0],'na shage: ', steps)

    print('summa: ',summa)
    globall = globall+summa
print('global: ', globall)
print('vsego elementov  ', list_of_steps)
listof_stepers = []
i =0
k =0
for i in range(len(list_of_steps)):
    k = k+1
    if list_of_steps[i] == 1:
        listof_stepers.append(k)
        k =0

a = [10,3,4,1,9]
a.sort()

listof_stepers.sort()
try:
    print('kol elementov shag do 18_19 : ', listof_stepers.index(19))
except:
    print('neudacha 19')
try:
    print('kol elementov shag do 18_20 : ', listof_stepers.index(20))
except:
    print('neudacha 20')

print('vsego elem hag : ', len(listof_stepers))

listof_stepers.reverse()

print('listof_stepers: ', listof_stepers)

# print('kol 1: ',list_of_steps.count(1))
# print('kol 2: ',list_of_steps.count(2))
# print('kol 3: ',list_of_steps.count(3))
# print('kol 4: ',list_of_steps.count(4))
# print('kol 5: ',list_of_steps.count(5))
# print('kol 6: ',list_of_steps.count(6))
# print('kol 7: ',list_of_steps.count(7))
# print('kol 8: ',list_of_steps.count(8))
# print('kol 9: ',list_of_steps.count(9))
# print('kol 10: ',list_of_steps.count(10))
# print('kol 11: ',list_of_steps.count(11))
# print('kol 12: ',list_of_steps.count(12))
# print('kol 13: ',list_of_steps.count(13))
# print('kol 14: ',list_of_steps.count(14))
# print('kol 15: ',list_of_steps.count(15))
# print('kol 16: ',list_of_steps.count(16))
# print('kol 17: ',list_of_steps.count(17))
# print('kol 18: ',list_of_steps.count(18))
# print('kol 19: ',list_of_steps.count(19))
# print('kol 20: ',list_of_steps.count(20))
# print('kol 20: ',list_of_steps.count(20))
# print('kol 21: ',list_of_steps.count(21))
# print('kol 22: ',list_of_steps.count(22))
# print('kol 23: ',list_of_steps.count(23))
# print('kol 24: ',list_of_steps.count(24))
# print('kol 25: ',list_of_steps.count(25))
# print('kol 26: ',list_of_steps.count(26))
# print('kol 27: ',list_of_steps.count(27))
# print('kol 28: ',list_of_steps.count(28))
# print('kol 29: ',list_of_steps.count(29))
# print('kol 30: ',list_of_steps.count(30))
# print('kol 31: ',list_of_steps.count(31))
# print('kol 32: ',list_of_steps.count(32))
# print('kol 33: ',list_of_steps.count(33))
# print('kol 34: ',list_of_steps.count(34))
# print('kol 35: ',list_of_steps.count(35))
# print('kol 36: ',list_of_steps.count(36))
# print('kol 37: ',list_of_steps.count(37))

print('sootnoshebie 1: ',round((len(list_of_steps))/(list_of_steps.count(1)),2))
print('sootnoshebie 2: ',round((len(list_of_steps))/(list_of_steps.count(2)),2))
print('sootnoshebie 3: ',round((len(list_of_steps))/(list_of_steps.count(3)),2))
print('sootnoshebie 4: ',round((len(list_of_steps))/(list_of_steps.count(4)),2))
print('sootnoshebie 5: ',round((len(list_of_steps))/(list_of_steps.count(5)),2))


print('vsego elementov  ', len(list_of_steps))