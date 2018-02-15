def lecnica():
    dobavka = 0
    stavka = 1
    postavleno = 0
    pribyl = 0
    i = 0
    for i in range(81):
        # postavleno = postavleno+stavka
        if i > -1 and i < 36:
            #dobavka = dobavka + 0.01
            print('dobavka: ',dobavka )
            postavleno = postavleno + stavka
            pribyl = (stavka ) * 36
        if i > 35 and i < 57:
            dobavka = dobavka + 0.04
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        if i > 56 and i < 66:
            dobavka = dobavka + 0.06
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        
        if i > 65 and i < 80:
            dobavka = dobavka + 0.08
            postavleno = postavleno + stavka + dobavka
            pribyl = (stavka + dobavka) * 36
        
        
        stavka2 = stavka + dobavka
        print('stavka', stavka + dobavka)
        
        
        print('shag:', i, ' kolichestvo postavlennogo:', postavleno, '  kompensacija: ', pribyl, 'raznica: ',
              round(pribyl - postavleno,2))


lecnica()