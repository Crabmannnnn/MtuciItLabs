#Задачи
#1. Определить класс Circle для представления круга.
#2. Использовать конструктор __init__ для инициализации радиуса круга (radius).
#3. Добаить метод get_radius(), который возвращает значение радиуса.
#4. Добавить метод set_radius(new_radius), который позволяет изменить радиус круга.
#5. Создайть объект класса Circle, измените его радиус и выведите новый радиус на экран

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_radius(self):
        return(self.radius)
    def set_radius(self,newradius):
        self.radius=newradius

ObjectCircle=Circle(10)
print(ObjectCircle.get_radius())
print(f"текущий радиус круга {ObjectCircle.get_radius()}")
newradius=input("Введите новый радиус")
ObjectCircle.set_radius(newradius)
print(f"текущий радиус круга {ObjectCircle.get_radius()}")
