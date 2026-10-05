numbers = [int(input()) for _ in range(5)]

print("исходный массив:", numbers)
max_number = numbers[0]
min_number = numbers[0]

#поиск максимального, минимального числа и суммы
for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
total = sum(numbers)

#Вывод результатов 
print(max_number, min_number, total)