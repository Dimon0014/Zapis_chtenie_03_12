def bolshee_in_12(tw_1,tw_2,tw_3):
    result = 0
    if tw_1>tw_2:
        if tw_1 > tw_3:
            result=1
        else:
            result = 3
    else:
        if tw_2 > tw_3:
            result = 2
        else:
            result = 3
    return result
bolshee=0
bolshee=bolshee_in_12(0,0,1)
print(bolshee)
