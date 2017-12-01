class Interv(object):
 genDict = {'activ_game':0}
 bank=200
 strategia=0
 var_of_risk=200
 steps_of_sesii=0
 def __init__(self, key):
  self.key_of_interval = key
  self.koiff_stavki = 1
  self.dict_of_interv={}
  self.interval =-1
  #self.strategia = strat
 def bank(self, bank,genDict):
     if genDict['activ_game'][0] == 0: #проверка на начало игры
      if bank<200:
        print('в банке нет минимума для игры')
        return 1
 def risk(self, var_of_risk, var):
     if var_of_risk > var:
        print(' превышен лимит риска игры')
        return 1
 def set_inerv_of_obj(self,inter):
	 self.interval= inter
 def namber_of_stavka(self, ):
	 pass
 

new_interv = Interv(25)
new_interv2 = Interv(25)
print(new_interv.strategia)
print(new_interv2.strategia)
new_interv2.strategia=24
print(new_interv.strategia)
print(new_interv2.strategia)