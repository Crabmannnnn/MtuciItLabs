#Задание
#1. Создайте класс Employee с общими атрибутами, такими как name (имя),id (идентификационный номер) и методами, например, get_info(),
#который возвращает базовую информацию о сотруднике.
#2. Создайте класс Manager с дополнительными атрибутами, такими как department (отдел) и методами, например, manage_project(),
#символизирующим управление проектами.
#3. Создайте класс Technician с уникальными атрибутами, такими как specialization (специализация), и методами, например,perform_maintenance(), означающим выполнение технического
#обслуживания.
#4. Создайте класс TechManager, который наследует как Manager, так и Technician.
#Этот класс должен комбинировать управленческие способности и технические навыки, например, иметь методы для управления проектами и выполнения технического обслуживания.
#5. Добавьте метод add_employee(), который позволяет TechManager добавлять сотрудников в список подчинённых.
#6. Реализуйте метод get_team_info(), который выводит информацию о всех подчинённых сотрудниках.
#7. Создайте объекты каждого класса и демонстрируйте их функциональность

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def get_info(self):
        return self.name,self.id
class Manager(Employee):
    def __init__(self,name,id,departament):
        Employee.__init__(self,name,id)
        self.departament=departament
    def manage_project(self):
        print(f"Менеджер {self.name} управляет проектом")
    def get_info(self):
        return self.name,self.id,self.departament
class Technican(Employee):
    def __init__(self,name,id,speciialization):
        Employee.__init__(self,name,id)
        self.specialization=speciialization
    def perform_maintenance(self):
        print(f"Техник {self.name} обслуживает оборудование")
    def get_info(self):
        return self.name,self.id,self.specialization
class TechManager(Manager,Technican):
    def __init__(self,name,id,speciialization,departament,employees,employeescount=0):
        Manager.__init__(self,name,id,departament)
        Technican.__init__(self,name,id,speciialization)
        self.employees=employees
        self.employeescount=employeescount
    def add_employee(self,employees):
        self.employees+=[employees]
        self.employeescount+=1
    def get_team_info(self):
        print("Информация о комманде:")
        for x in range(self.employeescount):
            info=self.employees[x]
            print(info.get_info())
            x+=1
mikky=Employee("Tom",1)
print("Информация о сотруднике:",mikky.get_info())
baz=Manager("Baz",2,"Space Department")
print("Информация о сотруднике:",baz.get_info())
baz.manage_project()
woody=Technican("Tom",3,"Cowboy")
print("Информация о сотруднике:",woody.get_info())
woody.perform_maintenance()
s=[]
disney=TechManager("Disney",0,"The main department","Managment",s)
print(disney.get_info())
disney.get_info
disney.perform_maintenance()
disney.manage_project()
disney.add_employee(mikky)
disney.add_employee(baz)
disney.get_team_info()
