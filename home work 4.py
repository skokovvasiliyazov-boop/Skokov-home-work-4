type = str(input("Введите тип учебгого материал: "))
price = float(input("Введите стоимость учебного материала: "))
well = input("Введите категорию  материала: ")
if type == "книга":
    print(type)
elif type == "фильм":
    print(type)
else:
    print("Тип-другое")
if price < 0:
    print("некорректная цена")
else:
    print(price)
if well == "математика":
    print(well)
elif well == "физика":
    print(well)
else:
    print("Категория-другое")
print("Материал добавлен: " "Тип =",type,",""Стоимость -",price,",""Категория -",well)
print("замена")