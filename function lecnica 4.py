def lecnica():
    dobavka = 0
    stavka = 0.01
    postavleno = 0
    pribyl = 0
    i = 0
    for i in range(112):
        # postavleno = postavleno+stavka
        if i > -1 and i < 36:
            # dobavka = dobavka + 0.01
            print('dobavka: ', dobavka)
            postavleno = postavleno + stavka
            pribyl = (stavka) * 36
        if i > 35 and i < 54:
            dobavka =  0.01
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 53 and i < 72:
            dobavka =  0.03
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36

        if i > 71 and i < 89:
            dobavka =  0.07
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 88 and i < 106:
            dobavka =  0.15
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 105 and i < 123:
            dobavka =  0.31
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36

        # if i > 81 and i < 88:
        #     dobavka =  0.05
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # if i > 87 and i < 93:
        #     dobavka =  0.06
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # if i > 92 and i < 97:
        #     dobavka =  0.07
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        #
        #
        # if i > 96 and i < 101:
        #     dobavka =  0.08
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # if i > 100 and i < 105:
        #     dobavka = 0.09
        #     postavleno = postavleno + stavka + dobavka
        #     pribyl = (stavka + dobavka) * 36
        # if i > 104 and i < 108:
        #     dobavka = 0.1
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


lecnica()