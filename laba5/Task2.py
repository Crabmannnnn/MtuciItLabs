#1. Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
#2. Добавьте метод get_info(), который возвращает информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]".

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
