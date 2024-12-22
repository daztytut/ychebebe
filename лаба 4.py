# 1
import math
import datetime

a = int(input("Введите число квадратный корень которого хотите вычислить: "))

current_datetime = datetime.datetime.now()

print(math.sqrt(a))

print(current_datetime)

print(int(math.sqrt(a)))
# 2
print("Введите число факториал которого Вы хотите найти:")
import my_module as mdl

a = int(input())

print(mdl.fact(a))
#3
from moduli import module2 as mdl2, module3 as mdl3

a = int(input("Введите 1 чтобы воспользоваться первым модулем и 2 чтобы воспользоваться вторым: "))

if (a == 1):
  c = int(input("Ведите цифру, квадрат которой Вы желаете найти: "))
  print(mdl2.hu(c))

elif (a == 2):
  m = int(input("Введите число, квадратный корень которого Вы хотите найти: "))
  print(mdl3.he(m))


else:
  print("Ошибка, программа не работает потому что Вы не поддерживаете Гитлера:(((( (фашизм это плохо!)")