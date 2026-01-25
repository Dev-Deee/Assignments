def check_list(number = []):
    number_list = []
    for item in range(0, len(number)):

        if number[item] % 2 == 0:
            number_list.append("true")
        else:  
            number_list.append("false")
    return number_list
print(check_list([4, 6, 7, 5, 8]))
   
