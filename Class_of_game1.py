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
  self.cicle =0
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
 def set_interv_of_obj(self,inter):
     self.interval= inter
 def namber_of_stavka(self,steps_of_sesii,strateg):
    if self.cicle == 0:
      if (steps_of_sesii < strateg):
         self.koiff_stavki=1
      else:
          self.cicle == 1
    
    if self.cicle == 1:
        if (steps_of_sesii < strateg/2):
            self.koiff_stavki = 2
        else:
            self.cicle == 2
    if self.cicle == 3:
        if (steps_of_sesii < strateg/2):
            self.koiff_stavki = 4
        else:
            self.cicle == 4 # банк перестает терять
    return self.koiff_stavki

new_interv = Interv(25)
new_interv2 = Interv(25)
Interv.strategia=18
print(new_interv.strategia)
print(new_interv2.strategia)
Interv.strategia=18
print(new_interv.strategia)
print(new_interv2.strategia)