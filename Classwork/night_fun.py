students = [
    ("Alice", 78),
    ("Bob", 45),
    ("Charlie", 90),
    ("Diana", 62),
    ("Kent", 30),
]

products = [
    ("laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 45),
    ("Monitor", 300),
    ("USB Cable", 10),
]

points = [
    (2, 3),
    (-1, 4),
    (5, -6),
    (0, 7),
    (-3, 0),
]

employees = [
("John", "IT", 50000),
("Jane", "HR", 45000),
("Mike", "IT", 60000),
("Sara", "Finance", 70000)
]

def unpack_score (score):
    for name, score in students:
        print(f"name: {name}, score: {score}")

def unpack_grade (grade):
    for name, grade in students:
        if grade >= 60:
            print(f"name: {name}, grade: {grade}")

def count_students_passed(grade):
    count = 0
    for name, score in students:
        if score >= 50:
            count += 1
    return count

def get_products_above_100(product):
    return product[1] > 100

def calculate_sum(product):
    sum = 0
    for product, price in products:
        sum += price
    return sum

def unpack_product(products):
    for product, price in products:
        print(f"Product: {product} - Price: {price}")

def get_positive_points(points):
    positive_points = []
    for point in points:
        pointA, pointB = point
        if pointA > 0 and pointB > 0:
            positive_points.append((pointA, pointB))
    return positive_points


# def get_high_earning_it_employees(employees):
#     it_employees = []
#     for employee in employees:
#         name, department, salary = employee
#         if department == "IT" and salary > 55000:
#             it_employees.append((name, department, salary))
#     return it_employees

def get_high_earning_it_employees(employees):
    return [employee for employee in employees if employee[1] == "IT" and employee[2] > 55000]


unpack_score(students)
unpack_grade(students)
print(count_students_passed(students))
print(list(filter(get_products_above_100, products)))
print(calculate_sum(products))
unpack_product(products)
print(get_positive_points(points))
print(get_high_earning_it_employees(employees))