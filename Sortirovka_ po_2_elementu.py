d = {(37,36):[ 1,[1, 2], 33],(37,35):[ 11,[101, 102], 31],(38,39):[ 21,[10, 12], 32] }
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = (sorted(d.items(), key=lambda t: t[1][2])) # работает по второму элементу
# OrderedDict([(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)])
print(sorted_x)