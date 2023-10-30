def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key


numbers_list = [12, 11, 13, 5, 6]

print("Original list:", numbers_list)
insertion_sort(numbers_list)
print("Sorted list:", numbers_list)