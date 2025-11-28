#Задачи:
#1. Определить базовый класс Vehicle с атрибутами: make (марка) и model (модель), а также методом get_info(), который возвращает информацию о транспортном средстве.
#2. Создать класс Car, наследующий от Vehicle, и добавить в него атрибут fuel_type (тип топлива)
# Переопределить метод get_info() таким образом, чтобы он включал информацию о типе топлива.

class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def get_info(self):
        return(self.make,self.model)
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)
        self.fuel_type=fuel_type
    def get_info(self):
        return(self.make,self.model,self.fuel_type)

testvehicle=Vehicle("Bycicle","223")
print(testvehicle.get_info())
testcar=Car("Camaz","0.39","Benzin")
print(testcar.get_info())
