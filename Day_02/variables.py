# Level 1

first_name = "Martin"
last_name = "Mathew"
full_name = "Martin Mathew"
country = "India"
city = "Kochi"
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True

# Multiple variables on one line
name, course, university = "Martin", "Full Stack AI Development", "Jain University"


# Level 2

# Check the data type of all variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Length of first name
print("Length of first name:", len(first_name))

# Compare length of first name and last name
print("Are the lengths equal?", len(first_name) == len(last_name))


# Arithmetic operations

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)


# Circle calculations

radius = 30

area_of_circle = 3.14159 * radius ** 2
circum_of_circle = 2 * 3.14159 * radius

print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)


# Take radius as user input and calculate area

user_radius = float(input("Enter radius of circle: "))

user_area = 3.14159 * user_radius ** 2

print("Area of circle:", user_area)


# Get user information

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
