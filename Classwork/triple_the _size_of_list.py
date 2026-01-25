def square_cube(number = []):
    number_list = []

    for items in range(0, len(number)):
        square_of_number = number[items] * number[items] 

        number_list.append(number[items])
        number_list.append(square_of_number) 

        cube_of_number =   square_of_number * number[items] 
        number_list.append(cube_of_number) 

    return number_list

print(square_cube([2, 3, 4]))
