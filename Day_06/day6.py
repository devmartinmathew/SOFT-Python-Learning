# 1. Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)


# 2. Create tuples of brothers and sisters
brothers = ("Arun", "Rahul")
sisters = ("Anu", "Meera")

print("Brothers:", brothers)
print("Sisters:", sisters)


# 3. Join brothers and sisters tuples
siblings = brothers + sisters
print("Siblings:", siblings)


# 4. How many siblings do you have?
print("Number of siblings:", len(siblings))


# 5. Add father and mother names and assign to family_members
parents = ("Father", "Mother")

family_members = siblings + parents

print("Family members:", family_members)

# 1. Unpack siblings and parents from family_members

family_members = ("Arun", "Rahul", "Anu", "Meera", "Father", "Mother")

*siblings, father, mother = family_members

print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)


# 2. Create fruits, vegetables and animal products tuples
# Join them and assign to food_stuff_tp

fruits = ("banana", "orange", "mango")
vegetables = ("carrot", "potato", "onion")
animal_products = ("milk", "meat", "butter")

food_stuff_tp = fruits + vegetables + animal_products

print("Food stuff tuple:", food_stuff_tp)


# 3. Convert food_stuff_tp tuple to a list

food_stuff_lt = list(food_stuff_tp)

print("Food stuff list:", food_stuff_lt)

# Python Tuples Practice
# Topics:
# 1. Creating a Tuple
# 2. Tuple Length
# 3. Accessing Tuple Items
# 4. Slicing Tuples
# 5. Changing Tuples to Lists
# 6. Checking an Item in a Tuple
# 7. Joining Tuples
# 8. Deleting Tuples


# --------------------------------------------------
# 1. Creating a Tuple
# --------------------------------------------------

empty_tuple = ()
print("Empty tuple:", empty_tuple)

fruits = ("banana", "orange", "mango", "lemon")
print("Fruits tuple:", fruits)

single_item_tuple = ("apple",)
print("Single item tuple:", single_item_tuple)


# --------------------------------------------------
# 2. Tuple Length
# --------------------------------------------------
print("Length of fruits tuple:", len(fruits))
