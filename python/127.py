numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    smallest = min(numbers)
    print("Smallest number:", smallest)
else:
    print("The list is empty.")