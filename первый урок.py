name = input("Как зовут этого толстячка? Введите ваше имя: ")
print("Привет," + name + "! \nЯ рассчитаю твою норму воды в мл на день")
weight = float(input("Введите ваш вес: "))
print(weight * 30)
if weight > 100:
    print(name + ", Ты просто бомба! Помни, хорошего человека должно быть много!")
else:
    print(name + ", Ты просто бомба! Кушай побольше!")
