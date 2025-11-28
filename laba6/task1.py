#1. Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами: имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password)
#2. Используйте конструктор __init__ для инициализации этих атрибутов.
#3. Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта.
#4. Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль текущему паролю аккаунта и возвращает True или False.
#5. Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его с помощью методов set_password и check_password.

class UserAccount:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.password=password
    def set_password(self,new_password):
         self.password=new_password
    def check_password(self,password):
        if self.password==password:
            return True
        else:
            return False

TestAcc=UserAccount("Mike","Chtoto@yandex","42")
password=input("Введите пароль")
if TestAcc.check_password(password)==True:
    new_password=input("Введите новый пароль")
    TestAcc.set_password(new_password)
    password=input("Новый пароль установлен, попробуйте ввести новый пароль")
    if TestAcc.check_password(password) == True:
        print("Правильно")
    else:
        print("Неверный пароль")
else:
    print("Неверный пароль")
