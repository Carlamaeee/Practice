numbers = []
for i in range(10):
    # Ask the user to input a number
    num =float(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("The entered numbers are:")
for num in numbers:
    print(num)
total_sum = 0

for num in numbers:
    total_sum += num
print(f"The sum of the entered numbers is: {total_sum}")
