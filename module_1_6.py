my_dict= {'Galina':1949, 'Andrey':1974, 'Maksim':1982, 'Semen':1994} # Созал словарь
print('Dict:', my_dict)
print('Existing value:',my_dict ['Semen']) # Вывел значения по существующему ключу
print('Not existing value:', my_dict.get ('Yulia')) # Вывел значения по не существующему ключу
my_dict.update({'Yulia' : 1993, 'Anastasiya' : 2015})#Добавил оновременно несколько ключей и значений
print('Modified dictionary:', my_dict)
print('Modified dictionary:', my_dict.update({'Yulia' : 1993, 'Anastasiya' : 2015}))  # Вот тут возникла проблемма, если я пишу 5 и 6 строку в одну строку то программа выдает 'None'
#в чем проблемма я не понимаю!
print('Deleted: ', my_dict.pop('Yulia'))
print(my_dict)
print(my_dict.items()) #Или можно отобразить вот таким способом
my_set = {1,2,3,5,5,6,1,2,'Петропавловск',True,} #Логический тип анных множество не отображает, в лкции bool тоже не отобразилось
print(my_set)
my_set.add(77)
my_set.add(33)
print(my_set)
my_set.discard(1)
print(my_set)