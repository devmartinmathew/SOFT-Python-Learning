first_name = 'Martin'
last_name = 'Mathew'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Anugraha S
full_name = first_name + space + last_name
print(full_name)  # Anugraha S
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 15

#### Unpacking characters 
# Unpacking characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
print(first_letter)  # P
second_letter = language[1]
print(second_letter) # y
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
print(last_letter)  # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
print(last_letter)  # n
second_last = language[-2]
print(second_last) # o
print(second_last)  # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
last_three = language[3:6]
print(last_three) # hon
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon


# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto
pto = language[0:6:2]
print(pto)  # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
print(challenge.endswith('tion'))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('th'))  # 0

# format()	formats string into nicer output    
# format()	formats string into nicer output
first_name = 'Anugraha'
last_name = 'S'
job = 'Student'
country = 'India'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Anugraha S. I am a Student. I live in India.
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # I am Anugraha S. I am a Student. I live in India.

radius = 10
pi = 3.14
area = pi # radius ## 2
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0
print(result)  # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('th'))  # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('th'))  # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal()) # False
print(num.isdecimal())  # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
print(challenge.isupper())  # True


# isnumeric():Checks numeric characters


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y')) # 5
print(challenge.strip('y'))  # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
print(challenge.split())  # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
print(challenge.title())  # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
  

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
print(challenge.startswith('thirty'))  # False
