numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
total_sum = 0
count = 0
for num in numbers:
    if num is not None:
        total_sum += num
        count += 1
average = total_sum / (count+1)
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average
        break
print("Измененный список:", numbers)
