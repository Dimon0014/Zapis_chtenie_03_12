for i in range(1,36):
    print(' if interval_'+str(i)+' < 120:')
    print('     if razresh_'+str(i)+':')
    print('         dict_tansf_'+str(i)+' = chislo_'+str(i)+'(razresh_'+str(i)+', key, dict_contr_'+str(i)+')')
    print('         Viigral = Viigral + dict_tansf_'+str(i)+'[0]')
    print('         Proigral = Proigral + dict_tansf_'+str(i)+'[1]')
    print('         razresh_'+str(i)+' = dict_tansf_'+str(i)+'[2]')
       
       
       
       
       
       
       
       
            # if interval_'+str(i)+' < 120:
            #
            #     if razresh_1:
            #         dict_tansf_1 = chislo_1(razresh_1, key, dict_contr_1)
            #         Viigral = Viigral + dict_tansf_1[0]
            #         Proigral = Proigral + dict_tansf_1[1]
            #         razresh_1 = dict_tansf_1[2]
          