#Задачи:
#1. Определить класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
#2. Добавить метод get_info(), который возвращает информацию о книге вформате: "Название книги: [title], Автор: [author], Год издания: [year]"
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def get_info(self):
        return(f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}")

CAndP=Book("CrimeAndPunishment","Dostoyevskiy",1866)
print(CAndP.get_info())
