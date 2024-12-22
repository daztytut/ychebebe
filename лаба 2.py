#zadanie 1
def greet(name):
    return "hello " + name

def square(number):
    return "Квадрат числа " + str(number) + " равен " + str(number**2)

def max_of_two(x,y):
    return "Максимальное число " + str(max(x,y))

print(greet("Миумявыч"), square(3), two_square(5), max_of_two(77,52))

#zadanie 2
def describe_person (name, age = 30):
    return "Имя " + name + " Возраст " + str(age)

print (describe_person("Миумявыч"), describe_person("Миумявыч", 825))
#zadanie 3
def is_prime(number):
    a = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            a += 1
    if (a > 2):
        return False
    else:
        return True


print(is_prime(16))