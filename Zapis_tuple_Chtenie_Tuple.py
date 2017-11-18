f = open('pro.txt', 'a')
h=[]
g = []
tip=(21, 11, 32, 22, 21, 25, 7)
h.append(tip)
h.append(tip)
h.append(tip)

print(h)

for item in h:
    print(item)
    f.write("%s\n" % str(item)) # здесь мы записываем в файл и добавляем строку переноса

p = open('pro.txt', 'r')
k = [line.strip() for line in p]
st=str(k)
st2=st.splitlines()
st3=st2[0]
print('st2',st2)
print('st3',st3)
print('k',k)
p2 = open('pro.txt', 'r')
for i, line in enumerate(p2): # мы здесь сразу добавляем в файл
	g.append(line)
	print(i, line)
print(g)
ak = k[2]
ak2 = g[0]
if hash(ak)== hash(ak2):
	print('равны')
	
	