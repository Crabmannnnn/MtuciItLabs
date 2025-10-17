def reading(readtype):
    with open(r'laba3/example.txt', 'r') as file:
        stroki = list(file)
    if readtype=="Строку":
        number=input("Какую строку вы хотите прочесть:")
        try:
            number=int(number)
            if(number<=len(stroki)):
                print(stroki[number-1])
            else:
                print("Некоректное значение строки")
        except ValueError:
            print("Некоректная строка")
    elif(readtype=="Строки"):
        print("Введите число строк которые вы хотите прочесть(Меньше",len(stroki),")")
        chislostrok=input()
        try:
            chislostrok=int(chislostrok)
            strokavubor=[str("")]*10
            for x in range(chislostrok):
                print("Введите строку",x+1)
                choise = input()
                choise=int(choise)
                slice=stroki[choise-1:choise]
                strokavubor[x]=slice
                if (x > len(stroki)):
                    print("Некоректное значение строки")
                    break
            for x in range(chislostrok):
                print(strokavubor[x])
        except ValueError :
            print("Некоректный ввод")
    elif readtype=="xy":
        x=input("Введите первую строку")
        y=input("введите вторую строку")
        try:
            x=int(x)
            y=int(y)
            if x>len(stroki) or y>len(stroki):
                print("Некоректное значение строк")
            else:
                for z in range(x-1,y):
                    print(stroki[z])
        except ValueError:
            print("Некоректный ввод")
    else:
        with open(r'laba3/example.txt', 'r') as file:
            print(file.read)
r=input("По умолчанию файл читается целиком.\nЕсли вы хотите прочитать одну строку, напишите 'Строку'\n Если вы хотите прочитать несколько строк, напишите 'Строки'\n Если вы хотите прочитать от строки x, до строки y, напишите 'xy'\n ")
reading(r)
