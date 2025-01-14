def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list by returning 0
    average = total / count
    return average

my_numbers = [10, 20, 30, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

#Alternative solution: Raise a custom exception
def calculate_average_exception(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    total = sum(numbers)
    return total / len(numbers)

try:
    result = calculate_average_exception([])
    print(f"The average is: {result}")
except ValueError as e:
    print(f"Error: {e}") 