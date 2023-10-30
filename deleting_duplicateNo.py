def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers_list = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]

print("Original list:", numbers_list)
unique_numbers = remove_duplicates(numbers_list)
print("List with duplicates removed:", unique_numbers)