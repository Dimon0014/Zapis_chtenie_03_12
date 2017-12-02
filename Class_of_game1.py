class Interv(object):
 genDict = {'activ_game':0}
 dict_of_game_numbs =[]
 bank=200
 win = False
 strategia=0
 var_of_risk=200
 steps_of_sesii=0
 def __init__(self, key):
  self.key_of_interval = key
  self.koiff_stavki = 1
  self.dict_of_interv={}
  self.interval =-1
  self.cicle =0
  Interv.dict_of_game_numbs.append(key)
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
     name_of_intrv=inter
     dictt={str(name_of_intrv):inter}
     #print('1 длина genDict ',name2 )
     Interv.genDict.update(dictt)
     # name4 = len(Interv.genDict)
     # print('2 длина genDict', name4)
     return self.interval
 def koiff_of_stavka(self,steps_of_sesii,strateg):
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



 def number_of_interval(self,inter,dict_ed):
  # print("self.interval:",self.interval)
  result=None
  for item in dict_ed:
      # print('item:',item)
      if dict_ed[item][0]==inter:
          result = dict_ed[item][3]
          break
  return result
 def stavka(self, key, inter, dict_ed):
    Interv.bank=Interv.bank - self.koiff_stavki
    nomer = self.number_of_interval(inter, dict_ed)

    Interv.dict_of_game_numbs.append(nomer)
 def func_ochistki_stavok(self, win,genDict, inter):
     if win:
         Interv.win = True
         genDict[inter] = 0

     else:

         genDict[inter]=1 # интервал в игре
     Interv.win = False

 def func_of_win(self, key,dict_of_game_numbs, strateg ): #функция должна стоять самой первой
   for numb in dict_of_game_numbs:
       if numb == key:
        print(" Выигравшее число: ",numb)
        win= strateg*self.koiff_stavki
        Interv.bank = Interv.bank + win
        Interv.win = True
       else:



key =14
intr =Interv(key)
dikktt =({(key): [12, [12,24], 1, key, 100]})
nomer = intr.number_of_interval(12,dikktt)
print('key',nomer)