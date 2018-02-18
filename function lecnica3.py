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


lecnica()