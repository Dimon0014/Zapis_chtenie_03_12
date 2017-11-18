class Dvoyki(object):
	"""docstring"""
	count = 0
	def __init__(self):
		"""Constructor"""
		# self.count = 0
		self.steps = [1]
		self.last_seen = 0
	    
	def count_f(self):
		Dvoyki.count += 1 # ура работает
	    #return vivod
	
	def steps_f(self):
		now_steps = self.count - self.steps[-1]
		self.steps.append(now_steps)
		self.last_seen = 0
	
	def last_seen_f(self):
		self.last_seen = self.last_seen + 1
		return self.last_seen
d00= Dvoyki()
for i in range(10):
	d00.count_f()
	if i%2 == 0:
		d00.steps_f()
	print('кол шагов d00',d00.count)
	print('последний раз вид. 00',d00.last_seen_f())

d01= Dvoyki()
for i in range(10):
	d01.count_f()
	if i%3 == 0:
		d01.steps_f()
	print('кол шагов d01',d01.count)
	print('последний раз вид. 01',d01.last_seen_f())

		
	