import json


class Dvoyki(object):
	"""docstring"""
	count = 0
	
	def __init__(self):
		"""Constructor"""
		# self.count = 0
		self.steps = [1]
		self.last_seen = 0
	
	def count_f(self):
		Dvoyki.count += 1  # ура работает
	
	# return vivod
	
	def steps_f(self):
		now_steps = self.count - self.steps[-1]
		self.steps.append(now_steps)
		self.last_seen = 0
	
	def last_seen_f(self):
		self.last_seen = self.last_seen + 1
		return self.last_seen


viborka = []
lst_vct2 = []
# востановление всех ходов
file_obj = open('100_xodov.txt')
data_list = file_obj.readlines()
for line in data_list:
    viborka.append(int(line))
# загрузка всех пар
with open('2sh.txt', 'r') as f:  # извлекаем  из файла
    data2 = json.load(f)

# print(data2)
data_fin2 = []
i = 0
for item in data2:  # приводим к типу Python
    data_fin2.append(tuple(item))

print('список кортежей 2', data_fin2)  # проверка готового результата

# подсчет количества выпаданий
z = 0
for i in range(len(viborka)):
    
    if i > 0:
        vec2 = (viborka[i - 1], viborka[i])
        for item in data_fin2:
            if hash(vec2) == hash(item):
                print('это-', vec2, z, "-", i)
                
            # print('список всех ходов из 100_ходов.тхт - до обработки',data_list)
            # print('список всех ходов из 100_ходов.тхт - посл. обработки',viborka)
