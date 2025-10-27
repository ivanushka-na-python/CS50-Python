# func and vars 
# аргументы - входные данные для функции 

'''
hello - три апострофа или двойных кавычек - тоже коммент - но использовать не удобно, если только не писать на нескольких строках
то что мы можем передать в func - параметры, что мы передаем в func - аргументы
sep и end - именованные параметры 
'''

# name = input('Whats your name? ').strip(',').title()
# # name = name.strip(',').title() # strip - это метод, не функция
# print(f'hello, {name}')


# name = input('Whats your name? ').strip().title() 
# first_name, surname = name.split(' ')
# print(f'hello, {first_name}')

# x = input('x ')
# y = input('y ')
# z = int(x) + int(y) # преобразуем строки в инт, любой ввод с клавы - строка
# print(z)

# x = int(input('x '))
# y = int(input('y '))
# print(x + y)


# x = float(input('x '))
# y = float(input('y '))
# z = round(x / y, 5) # вторым аргументом указываем до какого знака после точки округлять
# print (z) # round - округление, принимает число и аргкмент (до какого знака после точки нужно округлить)
# # print (f'{z:,}') # переносим запятую на три знака влево
# print (f'{z:.2f}') # переносим запятую на три знака влево при делении

# def hello(name):
#    print('hello', name)

# name = input('tell your name ')

# hello(name)

def main():
   name = input('tell your name ')
   hello(name)

def hello(name):
   print('hello', name)

main()
'''
определили основной кусок кода как функцию,
теперь не нужно доп функции писать изначально вверху а потом их вызывать
доп функции можно описывать после основного куска кода, 
передавая в функцию main доп функцию

paw (число, степень) функция возведения в степень
'''
