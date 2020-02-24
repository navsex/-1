# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.


second_time = int(input('Введите время в секундах: '))


hour = second_time // 3600              # ищем часы
minute = (second_time // 3600) // 60     # ищем минуты
second = second_time % 60               # ищем секунды

# if hour < 10 and minute < 10 and second < 10:   # если < 10 добавляем в переди 0
#     hour = '0'+str(hour)
#     minute = '0'+str(minute)
#     second = '0'+str(second)
hour = "%02d" % hour
minute = "%02d" % minute
second = "%02d" % second
print(hour +':' + minute + ':' + second)

################################################