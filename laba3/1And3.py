def reading(filename,MetodOfRead,line):
    if MetodOfRead=="ц":
        with open(filename, 'r') as file:
            content = file.read()
            return content
    elif MetodOfRead=="с":
        with open(filename, 'r') as file:
            content=0
            for x in range(0,line+1):
               content = file.readline()
            return content
    else:
        return "Некоректный способ чтения"
try:
    line=1
    filename=input("Введите название файла")
    readmetod=input("Если вы хотите прочитать файл целиком, введите 'ц', если вы хотите прочитать файл построчно, введите 'c'")
    if readmetod=="с":
        line = input("Сколько строк вы хотите прочитать?")
        try:
            line=int(line)
        except ValueError:
            print("Некоректное значение строки")
            line=0
    for x in range(0,line):
        print(reading(filename,readmetod,x),end='')
except FileNotFoundError:
    print("Некоректное название файла")
