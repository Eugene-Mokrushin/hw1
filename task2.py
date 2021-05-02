# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!


# Функция нахождения суммы цифр в числе
def sum_of_digits(number):
    digits_sum = 0
    while number > 0:
        reminder = number % 10
        digits_sum = digits_sum + reminder
        number = number // 10
    return digits_sum


# Создаем лист кубов из нечетных чисел
main_list = [integer ** 3 for integer in range(0, 1001) if integer % 2 != 0]
print(main_list)

# Нахоим сумму чисел, сумма цифр которых делится на 7
total_of_dev_seven = sum([integer for integer in main_list if sum_of_digits(integer) % 7 == 0])
print(total_of_dev_seven)

# Прибавляем 17 к каждому числу в списке
main_list = [integer + 17 for integer in main_list]
print(main_list)

# Находим сумму уже увеличенных чисел кратных 17
total_of_dev_seven = sum([integer for integer in main_list if sum_of_digits(integer) % 7 == 0])
print(total_of_dev_seven)
