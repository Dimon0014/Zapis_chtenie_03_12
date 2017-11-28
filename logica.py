import json
viborka=[]
lst_vct2=[]
file_obj = open('100_xodov.txt')
data_list = file_obj.readlines()
for line in data_list:
    viborka.append(int(line))
for i in range(len(viborka)):

    if i>0:
        vec2 = (viborka[i],viborka[i])
        
print(data_list)
print(viborka)



# with open('no.txt', 'r') as f: # извлекаем  из файла
#     data2 = json.load(f)
#
# #print(data2)
# data_fin=[]
# i=0
# for item in data2:              # приводим к типу Python
# 	data_fin.append(tuple(item))
#
# print(data_fin) # проверка готового результата


