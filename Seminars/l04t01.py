# 1). Задайте строку из набора чисел. Напишите программу, котораяя покажет большее и меньшее число.
# В качестве символа разделителя используйте пробел.

lst = [int(num) for num in input("Введите числа через пробел: ").split()]
print(lst)
print(min(lst))
print(max(lst))