### MINI CALCULATOR

## Introduction

 A calculator is a device that performs arithmetic operations on numbers. The simplest calculators can do only addition, subtraction, multiplication, and division. More sophisticated calculators can handle exponent ial operations, roots, logarithm s, trigonometric functions, and hyperbolic functions.
 The purpose of a calculator is to do correct calculations, and to do so efficiently. It is clear that a calculator should relieve the user of the need to do mental operations and of the need to rely on paper, so far as possible.
 
 ### Features
 
*  Addition
* Substraction
* Multiplication
*  Division
*  Square
*  Power
*  Square root

### Advantages

* Calculator can solve complicated problems quickly and in an efficient manner.
* Calculator gives more accurate resukts than counting manually.
* Calcultor has all formulas for counting process and makes the counting process easier.
* useful to convert the units of measurements.

### Disadvantages

* People will be dependant on usong calculators for counting.
* Calculator limits the knowledge of the users.
* People will be unable to memorize the process of problem solving.
* Student will not know how to get the result of their questions. 


## Swot Analysis

![SWOT ANALYSIS](https://user-images.githubusercontent.com/94373133/152027690-9120219c-a7f0-4db9-8213-4e5ff1dacbbe.jpeg)

## 4W's 1H

### Who
* user/ who want 
### What
* To calculate 
### When
* During the need of calculation
### Where
* Laptop, shop, bill generation etc
### How
* By entering the numbers.


## High Level Requirements
| ID | Description | 
| --- | --- | 
| HR01 | System should be able to get the  first number|
| HR02 | User should be able to get the second number  | 
| HR03 | System should recognize the operations | 


## Low Level Requirement
| ID | Description | 
| --- | --- | 
| LR01 | System should able to do the addition | 
| LR02 | System should able to do the substraction |
| LR03 | System should able to do the multiplication | 
| LR04 | System should able to do the all operations | 

# HIGH LEVEL DESIGN
![c1](https://user-images.githubusercontent.com/94373133/152172369-913a9444-f420-4e5c-9e4d-04eca6435669.png)
# LOW LEVEL DESIGN
![C2 drawio (1)](https://user-images.githubusercontent.com/94373133/152176727-254d21de-b4ab-4ca7-8e11-99fd0a42b90c.png)


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
