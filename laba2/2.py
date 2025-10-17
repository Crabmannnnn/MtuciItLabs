def describe_person(name, age=30):
    print(name,"это человек, возраста", age, "лет")
name=input("Введите ваше имя:")
age=input("Введите ваш возвраст:")
try:
    int(age)
    describe_person(name,age)
except ValueError:
    describe_person(name)
