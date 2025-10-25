def addtext(filename,neworold,text):
    if neworold=="old":
        with open(filename,'a') as file:
            file.write(text+'\n')
    else:
        with open(filename,'w') as file:
            file.write(text + '\n')

filename=input("Введите название файла")
text=input("Введите текст который хотите добавить в файл")
try:
    file=open(filename,'r')
    file.close
    neworold="old"
    addtext(filename,neworold,text)
except FileNotFoundError:
    neworold="new"
    addtext(filename,neworold,text)
with open(filename,'r') as file:
      content=file.read()
      print(content)
