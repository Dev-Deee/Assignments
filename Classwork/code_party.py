from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9]
score = (1,2,3,4,5,6,7,8,9)
number_in_tuple = (1,2,[3,4],5)
fruit = ("apple", "banana", "cherry")
digits = (10, 20, 30, 40)
sample_input = [[2,3,4], [1,5,7], [4,6,8]]
sample_price = [100, 200, 300, 400]
tuple_list = [(1,'A'), (4, 'B'), (2,'C')]
lists = ["apple", "banana", "cherry", "madam", "c++"]
words = ["I", "love", "Python"]
number_of_numbers = [1,2,3,4]

def add_number_to_tuple():
    new_number = list(score)
    new_number.append(10)
    return (new_number)

def change_element_in_a_tuple():
    number_in_tuple[2][1] = 99
    return number_in_tuple

def convert_tuple_to_list():
    new_fruit_list = list(fruit)
    new_fruit_list.append("mango")
    return new_fruit_list

def unpack_tuple():
    number_one, number_two, *other_variable = digits
    return number_one, number_two, other_variable

def sum_row():
    return [sum(number) for number in sample_input]

def sum_column(input_one, input_two):
    return [input_one[number] + input_two[number] for number in range(len(input_one))]

def even_number(input):
    return input % 2 == 0

def check_length_of_string(input):
    return len(input) > 5

def check_value_in_tuple(tuple_list):
    return tuple_list[0] > 2

def check_number_divisible(input):
    return input % 3 == 0 and input % 5 == 0

def palindrome(input):
    return input == input[::-1]

def convert_string_to_uppercase(lists):
    return lists.upper()

def calculate_square_numbers(numbers):
    return numbers ** 2

def capitalize_first_letter(input):
    return input.capitalize()

def calculate_percentage(input):
    return input + input * (10 /100)

def sum_numbers(number_one, number_two):
    return number_one + number_two

def find_maximum_number(input_one, input_two):
        if input_one > input_two:
            return input_one
        else:
            return input_two

def concatenate_string(input_one, input_two):
    return input_one + input_two

def square_and_product(input_one, input_two):
    return input_one * input_two

def product_of_numbers(input_one):
    return input_one ** 2







print(reduce(square_and_product,(list(map(product_of_numbers, number_of_numbers)))))
print(reduce(find_maximum_number, sample_price))
print(reduce(concatenate_string, words))
print(reduce(sum_numbers, range(1, 51)))
print(list(map(calculate_percentage, sample_price)))
print(list(map(capitalize_first_letter, lists)))
print(list(map(calculate_square_numbers, range(1, 10))))
print(list(map(check_number_divisible, range(1, 51))))
print(list(map(convert_string_to_uppercase, lists)))
print(list(filter(palindrome, lists)))
print(list(filter(check_number_divisible, range(1, 51))))
print(list(filter(check_value_in_tuple, tuple_list)))
print(list(filter(check_length_of_string, fruit)))
print(list(filter(even_number, range(1, 21))))
print(sum_row())
print(reduce(sum_column, sample_input))
print(unpack_tuple())
print(convert_tuple_to_list())
print(change_element_in_a_tuple())
print(add_number_to_tuple())