

# Q1: Take multiple integer values entered by the user, add them and print out the result.
def add_integers():
    count = 0
    addition = 0
    integer_count = int(input('How many numbers do you want to add? '))
    while count < integer_count:
        numbers = int(input('Enter the numbers you want to add: '))
        addition += numbers
        count += 1
    #print(f'The sum of numbers is {add_numbers}')
    return addition
    
# addition = add_integers()
# print(addition)


# Q2: Take multiple integer values entered by the user, do a subtraction on them in the 
# order they are entered and print out the result.

def subtract_integers():
    count = 0
    subtract_numbers = 0
    integer_count = int(input('How many numbers do you want to subtract? '))
    first_number = int(input('Enter the start number to subtract from: '))
    while count < integer_count:
        numbers = int(input('Enter the numbers for subtraction: '))
        subtract_numbers -= numbers
        count += 1
    subtraction = first_number + subtract_numbers
    # print(f'The result of the subtraction operation gives, {Subtraction}')
    return subtraction


# subtraction = subtract_integers()
# print(subtraction)


# Q3: Take multiple integer values entered by the user, multiply them and print out the result. 

def multiply_integers():
    count = 0
    multiplication = 1
    integer_count = int(input('How many numbers do you want to multiply? '))
    while count < integer_count:
        numbers = int(input(' Enter the numbers to multiply: '))
        multiplication *= numbers
        count += 1
    # print(f'The mulitples of {integer_count} numbers is {multiply_numbers}')
    return multiplication

# multiplication = multiply_integers()
# print(multiplication)

# Q4: Take only two integer values entered by the user divide the first number by the 
# second and print out the result. Account for infinite value error (division by zero). 

def divide_integers():
    dividend = int(input('Enter the first number: '))
    divisor = int(input('Enter the second number: '))
    if dividend == 0 or divisor == 0:
        print('Please check you dont have a zero value!!')
    else:
        division = dividend / divisor
    return division

# division = divide_integers()
# print(f' The division operation of the integers is {division}')


# Q5: Take multiple integer values entered by the user and compute their average.
def get_average_number():
    count = 0
    total_num = 0
    average = 0
    integer_count = int(input(' How many numbers do you want to find the average? '))
    while count < integer_count:
        numbers = int(input(' Enter the numbers for average operation: '))
        total_num += numbers
        average = total_num /integer_count
        count += 1
    #print(f'The average of {integer_count} numbers is {average}')
    return average

# average = get_average_number()
# print(average)


#  Now let's combine all the individual operational functions under a function

def calculator_app():
    calculator = input('Enter addition, subtraction, multiplication, division or average operation? ').lower()
    if calculator == 'addition':
        operation = add_integers()
    elif calculator == 'subtraction':
        operation = subtract_integers()
    elif calculator =='multiplication':
        operation = multiply_integers()
    elif calculator == 'division':
        operation = divide_integers()
    elif calculator == 'average': 
        operation= get_average_number()
    print(f'The {calculator} operation, gives {operation} ')
    return operation

operation = calculator_app()
#print(operation)





                        
    
