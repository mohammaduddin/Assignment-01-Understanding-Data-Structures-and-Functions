# Problem: 01
# Write a function that takes two numbers as input and returns their average.
# Call the function with different values.
# commit-avg-result-calculation
def avg_calculation(num1, num2):
    """ this function takes two numbers as user input and returns their average """
    average = (num1 + num2)/2
    return average


# get inputs from user
first_num = float(input("Enter 1st number: "))
second_num = float(input("Enter 2nd number: "))

# call the function with arguments
result = avg_calculation(first_num, second_num)
print(f"The average of {first_num} and {second_num} is: {result}")








