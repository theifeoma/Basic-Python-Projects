#script that accepts input from user and stores in a list to print out the numbers typed, average of the numbers and the count of numbers typed.

#program will terminate when "done" is typed.

total = 0
values = []
while True:
    numbers = input("Enter number: ")
    if numbers == 'done':
        break
    try:
        number = int(numbers)
        values.append(number)
    except:
        print("Invalid Input!")

total = str(sum(values))
average = str(float(total) / len(values))
print("Numbers typed are " + str(values))
print("Total: " + total + " Count: " + str(len(average)) + " Average: " + str(average))

