


def chislo_01(razresh_01, key, dict_contr_01):
     win=0
     proig=0
     spisok=[0,0,True]
     result=[]
     if razresh_01:
         if key ==1:
             win=36*dict_contr_01["koef"]
             razresh_01 =False
             dict_contr_01["step"]=0
             dict_contr_01["koef"]=1
             spisok[0] = win
             spisok[2] = razresh_01
         else:
             razresh_01 = True
             dict_contr_01["step"]=dict_contr_01["step"]+1
             if dict_contr_01["step"]==36:
                 dict_contr_01["koef"]=dict_contr_01["koef"]*2

             if dict_contr_01["step"] ==54:
                 dict_contr_01["koef"] = dict_contr_01["koef"] * 2
             if dict_contr_01["step"] ==72:
                 dict_contr_01["koef"] = dict_contr_01["koef"] * 2
             if dict_contr_01["step"] == 90:
                 razresh_01 = False
             proig=proig-dict_contr_01["koef"]
             spisok[0]=win
             spisok[1]=proig
             spisok[2] = razresh_01
     return spisok