def lecnica():
    dobavka =0
    stavka =1
    postavleno = 0
    pribyl =0
    i=0
    for i in range(1000):
        # postavleno = postavleno+stavka
        if i> -1 and i< 37 :
           dobavka = dobavka+0.01
     
           postavleno = postavleno + stavka + 0.01
        if i> 36 and i<74:
           dobavka = dobavka+0.02
           postavleno = postavleno + stavka + 0.02
        if i> 75 and i<1000:
           dobavka = dobavka+0.03
           postavleno = postavleno + stavka + 0.03
        stavka2 =stavka+dobavka
        print('stavka',stavka+dobavka)
        pribyl = (stavka+dobavka)*36
        
        print('shag:',i,' kolichestvo postavlennogo:',postavleno, '  kompensacija: ',pribyl, 'raznica: ', pribyl - postavleno)
lecnica()