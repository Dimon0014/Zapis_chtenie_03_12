def lecnica():
    dobavka = 0
    stavka = 0.01
    postavleno = 0
    pribyl = 0
    bufer =0
    ubyl = 0
    k = 0
    i = 0
    for i in range(1,200):
        if i< 44:
            bufer = bufer +1
            print('stavka: ',bufer)
            ubyl = ubyl +bufer
            print(i, 'ubyl:', ubyl, 'pribyl: ',bufer*35, 'hfznica: ',bufer*35- ubyl )
        if (i > 43) and (i < 57):
            bufer = bufer + 2
            print('stavka: ', bufer)
            ubyl = ubyl + bufer
            print(i, 'ubyl:', ubyl, 'pribyl: ', bufer * 35, 'hfznica: ', bufer * 35 - ubyl)

        if (i > 56) and (i < 70):
            bufer = bufer + 3
            print('stavka: ', bufer)
            ubyl = ubyl + bufer
            print(i, 'ubyl:', ubyl, 'pribyl: ', bufer * 35, 'hfznica: ', bufer * 35 - ubyl)
        if (i > 69)and (i < 78) :
            bufer = bufer + 4
            print('stavka: ', bufer)
            ubyl = ubyl + bufer
            print(i, 'ubyl:', ubyl, 'pribyl: ', bufer * 35, 'hfznica: ', bufer * 35 - ubyl)
        if (i > 77) and (i < 85):
            bufer = bufer + 5
            print('stavka: ', bufer)
            ubyl = ubyl + bufer
            print(i, 'ubyl:', ubyl, 'pribyl: ', bufer * 35, 'hfznica: ', bufer * 35 - ubyl)
        if (i > 84) and (i < 113):
            bufer = bufer + 6
            print('stavka: ', bufer)
            ubyl = ubyl + bufer
            print(i, 'ubyl:', ubyl, 'pribyl: ', bufer * 35, 'hfznica: ', bufer * 35 - ubyl)
                # postavleno = postavleno+stavka

        # stavka2 = stavka + dobavka
        # print('stavka', stavka + dobavka)

        # print('shag:', i, ' kolichestvo postavlennogo:', postavleno, '  kompensacija: ', pribyl, 'raznica: ',
        #       round(pribyl - postavleno, 2))


lecnica()