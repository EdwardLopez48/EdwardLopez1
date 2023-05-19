def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        median = (sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2
    else:
        median = sorted_numbers[length // 2]
    return median

# Prompt the user to enter a list of numbers
input_list = input("Enter a list of numbers separated by spaces: ")
numbers = input_list.split()
numbers = [float(num) for num in numbers]

# Find the median of the numbers
median = find_median(numbers)

# Display the result
print(f"The median of the numbers is: {median}")
