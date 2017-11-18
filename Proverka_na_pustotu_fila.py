file_obj = open('101_xodov.txt', 'w')
file_obj.close()
file_obj = open('101_xodov.txt', 'r')
t=file_obj.read()
file_obj.close()
if not t:  # если t равно False, конструкция not t возращает True
 print('Пустая строка')
 