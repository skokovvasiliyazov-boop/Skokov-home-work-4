"""
Найти сумму чисел заданого итервала
"""
num1 = int(input("Ведите первое значение: "))
num2 = int(input("Ведите второе значение: "))
if num1 > num2:
    num1, num2=num2, num1
j = 0
while num1 <= num2:
    j+=num1
    num1+=1
print("сумма: ",j, end="")
print()

"""
Найти наибольший общий делитель двух чисел
"""
a1 = int(input("Ведите первое значение: "))
b1 = int(input("Ведите второе значение: "))
while b1!=0:
    o=b1
    b1=a1%b1
    a1=o
    print("наибольший общий делитель: ",a1)

"""
Найти все делители числа
"""
number = int(input("Ведите значение: "))
j1=1
if number <= 0:
    print("введите чистло больше 0")
while j1 <= number:
    if number%j1==0:
        print("делитель",j1, end=" ")
        j1=j1+1
