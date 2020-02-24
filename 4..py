# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

# number = int(input('Введите число: '))

number = list(input('Введите число: ')) # создаем лист
print(number)
print(type(number))

for i in range(len(number)):
    number[i] = int(number[i]) # переводим из str  в int

print(number)
print(type(number))

number.sort()
print(number)

print(number[-1]) # НЕ ПРИДУМАЛ КАК ПО ДРУГОМУ!!!!!

################################################
#
