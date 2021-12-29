# Variable declaration, initialize integer number
num1 = 42
# Variable declaration, initialize floating point number
num2 = 2.3
# Variable declaration, initialize Boolean law
boolean = True
# Variable declaration, initialize string
string = 'Hello World'
# Variable declaration, initialize list of strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Variable declaration, initialize dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# Variable declaration, initialize tuple
fruit = ('blueberry', 'strawberry', 'banana')
# outputs what type of data (fruit) is.
print(type(fruit))
# outputs index 1 value
print(pizza_toppings[1])
# adds 'Mushrooms' in the end of the list
pizza_toppings.append('Mushrooms')
# outputs dictionary value
print(person['name'])
# assign/change value in dictionary
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])
# conditional statements if, else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# conditional statements if, else if, else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# for loop
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
# while loop
x = 0
while(x < 5):
    print(x)
    x += 1
# remove last item from list
pizza_toppings.pop()
# remove specific value by using index
pizza_toppings.pop(1)

print(person)
# remove specific value by using value
person.pop('eye_color')
print(person)
# for loop with conditional statements
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# definition declaration 
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
# definition declaration, initialize argument
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
# assign value to argument
print_hello_x_times(4)
# definition declaration, variable declaration, initialize argument, assign value to argument
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# outputs 'hello'
print_hello_x_or_ten_times()
# outputs 'hello', 'hello','hello','hello'
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

print(num3) # NameError: name <variable name> is not defined
num3 = 72 # num3 has never been called.
fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) # KeyError: 'favorite_team'
print(pizza_toppings[7]) # IndexError: list index out of range
    print(boolean) # IndentationError: unexpected indent
fruit.append('raspberry')# AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) # AttributeError: 'tuple' object has no attribute 'pop'