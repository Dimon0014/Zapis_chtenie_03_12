from operator import itemgetter
from collections import OrderedDict
d = {(37,36):[ 1,[1, 2], 33],(37,35):[ 11,[101, 102], 31]}
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = (sorted(d.items(), key=lambda t: t[1][2])) # работает по последней цифре из списка
# OrderedDict([(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)])
print(sorted_x)
sorted_x = (sorted(d.items(),reverse=True, key=lambda t: t[1][2]))# работает по последней цифре из списка, а потом выдает с конца
print(sorted_x)
#print(sorted_x[0][0]) #  вытаскиваем первый ключ
#print(sorted_x[1][0]) #  вытаскиваем второй ключ