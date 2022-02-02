def add(num1, num2):
    return num1 + num2


# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

def modulus(num1, num2):
    return num1 % num2

def square(num1):
    return num1 * num1

def power(num1,num2):
    return num1 * num2


def cube(num1):
    return num1 * 3

def square_root(num1):
    return num1 ** 0.5

print("Please select operation -\n" \
      "1. Addition\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      "5. Modulus\n" \
      "6. Square\n" \
      "7. Power\n" \
      "8. Cube\n" \
      "9. Square_root\n" )

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 ,5,6,7,8,9:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))

elif select == 5:
    print(number_1, "%", number_2, "=",
          modulus(number_1, number_2))

elif select == 6:
    print(number_1, "^", 2, "=",
          square(number_1))

elif select == 7:
        print(number_1, "*", number_2, "=",
              power(number_1, number_2))

elif select == 8:
        print(number_1, "^", 3, "=",
              cube(number_1))

elif select == 9:
        print(number_1,square_root ,"=",
              square_root(number_1))

else:
    print("Invalid input")