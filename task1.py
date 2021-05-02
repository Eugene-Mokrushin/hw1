user_number = int(input('Введите кол-во секунд: '))
century = user_number // 3154000000
user_number -= century * 3154000000
decade = user_number // 315400000
user_number -= decade * 315400000
year = user_number // 31540000
user_number -= year * 31540000
month = user_number // 2628336
user_number -= month * 2628336
day = user_number // 86410
user_number -= day * 86410
hour = user_number // 3600
user_number -= hour * 3600
minutes = user_number // 60
user_number -= minutes * 60
print(f'{century} век {decade} декад {year} лет {month} мес {day} дн {hour} час {minutes} мин {user_number} сек')

