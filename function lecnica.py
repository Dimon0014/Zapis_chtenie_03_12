def lecnica():
    dobaka =0
    stavka =1
    postavleno = 0
    pribyl =0
    i=0
    for i in range(108):
        # postavleno = postavleno+stavka
        if i< 37:
           dobaka = dobaka+0.01
           postavleno = postavleno + stavka + 0.01
        if i> 36 and i<73:
           dobaka = dobaka+0.02
           postavleno = postavleno + stavka + 0.02
        if i> 72 and i<108:
           dobaka = dobaka+0.03
           postavleno = postavleno + stavka + 0.03

        pribyl = (stavka+dobaka)*36
        print('shag:',i,' kolichestvo postavlennogo:',postavleno, '  kompensacija: ',pribyl, 'raznica: ', pribyl - postavleno)
lecnica()