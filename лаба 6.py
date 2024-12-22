#1 задание:
class UserAccount:
    def __init__(self, username, email, passw):
        self.username = username #публичные атрибуты
        self.email = email
        self.__password = passw #приватный атрибут - инкапсулирование

    def set_password(self, new_password):
        self.__password = new_password #присваеваем новый пароль

    def check_password (self, check_password):
        return self.__password == check_password #проверяем

NewUser = UserAccount("bibiziana", "bibiziana_bibi@mail.ru", "swegswegswegRus543280!!!_")
print (NewUser.check_password("swegswegswegRus543280!!!_")) #создаём экземпляр и проверяем его на валидность(правильность)

NewUser.set_password("IaIa678_9503!Kar")
print (NewUser.check_password("IaIa678_9503!Kar"))
# устанавливаем новый пароль и проверяем его

#ЗАДАНИЕ 2
class Vehile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    # создаём класс вехиль с атрибутами модели и марки
    def get_info(self):
        return f'Марка: {self.make}\nМодель: {self.model}'
#получ инф по марке и моделе

class Car(Vehile):
    def __init__(self, make, model, fuel):
        super().__init__(make, model)  #инициализируем старый класс (бох)
        self.fuel = fuel
# создаём класс машины дочерний класс от вехиля
    def get_info(self):
        return super().get_info() + '\n' + f'Топливо: {self.fuel}'
# вызывает метод гет инфо от родительского класса + топлива и выводим информацию

new_car = Car("Mazda", "6", "95")
print(new_car.get_info())
# создаём экземп класса кар и вызывает гет инфо