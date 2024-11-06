#Написать программу, которая:

#Создаёт с помощью генератора списков, список случайных целых чисел от -50 до 50 размером 25 элементов.
#Находит количество положительных, отрицательных и нулевых элементов в списке.
#Выводит значения и их (положительных, отрицательных и нулевых) количество вместе с процентом от общего количества.
#Выводит самое большое и самое маленькое значение


import random
arr = [random.randint(-50,50) for i in range (25)]

pol = 0 
ot = 0
n = 0
min = 50
max = -50

arr_pol = list()
arr_ot = list()
arr_n = list()

for el in arr:
    if el > 0:
        pol+=1
        arr_pol.append(el)
    elif el < 0:
        ot+=1
        arr_ot.append(el)

    else:
        n+=1
        arr_n.append(el)


print("Количество нулей: ",n,"Процент от общего количества: ",n/25*100)
print(arr_n)

print("Количество положительных чисел: ",pol,"Процент от общего количества: ",pol/25*100)
print(arr_pol)

print("Количество отрицательных чисел: ",ot,"Процент от общего количества: ",ot/25*100)
print(arr_ot)

for i in range(25):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print("Минимальный элемент = ",min)
print("Максимальный элемент = ",max)
