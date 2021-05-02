#  Реализовать склонение слова «процент» для чисел до 20.
#  Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
#  Вывести все склонения для проверки.
import random


percent = random.randint(0, 100)
# процент процентов процента
if percent % 10 == 1 and percent != 11:
    declension = 'процент'
elif percent % 10 in (2, 3, 4) and percent not in (12, 13, 14):
    declension = 'процента'
else:
    declension = 'процентов'

print(percent, declension)
