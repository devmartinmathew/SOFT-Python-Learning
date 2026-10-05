# Given set
it_companies = {
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
}


# 1. Find the length of the set
print("Number of IT companies:", len(it_companies))


# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)


# 3. Insert multiple IT companies at once
it_companies.update(["Netflix", "Tesla", "Adobe"])

print("After adding multiple companies:", it_companies)


# 4. Remove one company from the set
it_companies.remove("IBM")

print("After removing IBM:", it_companies)


# 5. Difference between remove() and discard()

# remove()
companies = {"Google", "Apple"}

companies.remove("Microsoft")
# KeyError because Microsoft is not in the set
# Gives an error if the item does not exist

# discard()
companies = {"Google", "Apple"}

companies.discard("Microsoft")
# No error
# Does not give an error if the item does not exist


# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


# 1. Join A and B
joined = A.union(B)
print("A union B:", joined)


# 2. Find A intersection B
intersection = A.intersection(B)
print("A intersection B:", intersection)


# 3. Is A subset of B
print("Is A subset of B?", A.issubset(B))


# 4. Are A and B disjoint sets
print("Are A and B disjoint?", A.isdisjoint(B))


# 5. Join A with B and B with A
print("A union B:", A.union(B))
print("B union A:", B.union(A))


# 6. Symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference:", symmetric_difference)


# 7. Delete the sets completely
del A
del B

# 1. Convert ages to a set and compare the length

ages = [22, 19, 24, 25, 26, 24, 25, 24]

ages_set = set(ages)

print("Length of list:", len(ages))
print("Length of set:", len(ages_set))

if len(ages) > len(ages_set):
    print("The list is bigger")
elif len(ages) < len(ages_set):
    print("The set is bigger")
else:
    print("Both are equal")

    # Python Sets Practice
# Topics:
# 1. Creating a Set
# 2. Getting Set's Length
# 3. Accessing Items in a Set
# 4. Checking an Item
# 5. Adding Items to a Set
# 6. Removing Items from a Set
# 7. Clearing Items in a Set
# 8. Deleting a Set
# 9. Converting List to Set
# 10. Joining Sets
# 11. Finding Intersection Items
# 12. Checking Subset and Super Set
# 13. Checking the Difference Between Two Sets
# 14. Finding Symmetric Difference Between Two Sets


# --------------------------------------------------
# 1. Creating a Set
# --------------------------------------------------

empty_set = set()
print("Empty set:", empty_set)

fruits = {"banana", "orange", "mango", "lemon"}
print("Fruits set:", fruits)


# --------------------------------------------------
# 2. Getting Set's Length
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}
print("Number of fruits:", len(fruits))


# --------------------------------------------------
# 3. Accessing Items in a Set
# --------------------------------------------------

# Sets are unordered, so we cannot access items using an index.
# We can loop through the set instead.

fruits = {"banana", "orange", "mango", "lemon"}

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 4. Checking an Item
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

print("Is banana in fruits?", "banana" in fruits)
print("Is apple in fruits?", "apple" in fruits)


# --------------------------------------------------
# 5. Adding Items to a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

fruits.add("apple")
print("After add:", fruits)

fruits.update(["lime", "grape"])
print("After update:", fruits)


# --------------------------------------------------
# 6. Removing Items from a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("orange")
print("After discard:", fruits)


# --------------------------------------------------
# 7. Clearing Items in a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

fruits.clear()
print("After clear:", fruits)


# --------------------------------------------------
# 8. Deleting a Set
# --------------------------------------------------

fruits = {"banana", "orange", "mango", "lemon"}

del fruits

# print(fruits)
# This would give NameError because the set is deleted.


# --------------------------------------------------
# 9. Converting List to Set
# --------------------------------------------------

fruits_list = ["banana", "orange", "mango", "banana", "lemon"]

fruits_set = set(fruits_list)

print("List:", fruits_list)
print("Converted set:", fruits_set)


# --------------------------------------------------
# 10. Joining Sets
# --------------------------------------------------

fruits = {"banana", "orange", "mango"}
vegetables = {"carrot", "potato", "onion"}

food = fruits.union(vegetables)
print("Using union:", food)

fruits.update(vegetables)
print("Using update:", fruits)


# --------------------------------------------------
# 11. Finding Intersection Items
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

common_items = set_a.intersection(set_b)

print("Intersection:", common_items)


# --------------------------------------------------
# 12. Checking Subset and Super Set
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {2, 3}

print("Is set_b a subset of set_a?", set_b.issubset(set_a))
print("Is set_a a superset of set_b?", set_a.issuperset(set_b))


# --------------------------------------------------
# 13. Checking the Difference Between Two Sets
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print("Difference A - B:", set_a.difference(set_b))
print("Difference B - A:", set_b.difference(set_a))


# --------------------------------------------------
# 14. Finding Symmetric Difference Between Two Sets
# --------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

symmetric = set_a.symmetric_difference(set_b)

print("Symmetric difference:", symmetric)


# --------------------------------------------------
# Extra Practice Problems
# --------------------------------------------------

# Problem 1:
# Create a set of five countries and print its length.

countries = {"India", "Japan", "Canada", "Germany", "Brazil"}
print("Countries:", countries)
print("Number of countries:", len(countries))


# Problem 2:
# Add a new country to the set.

countries.add("Australia")
print("After adding:", countries)


# Problem 3:
# Remove one country from the set.

countries.discard("Japan")
print("After removing Japan:", countries)


# Problem 4:
# Check if India exists in the set.

print("Is India in countries?", "India" in countries)


# Problem 5:
# Find common items between two sets.

python_students = {"Fayas", "Arun", "Rahul"}
javascript_students = {"Rahul", "Meera", "Fayas"}

common_students = python_students.intersection(javascript_students)

print("Common students:", common_students)


# Problem 6:
# Find all unique students from both sets.

all_students = python_students.union(javascript_students)

print("All students:", all_students)


# Problem 7:
# Find students who are in only one of the two sets.

unique_students = python_students.symmetric_difference(javascript_students)

print("Students in only one set:", unique_students)
