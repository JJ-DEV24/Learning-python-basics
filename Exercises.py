"""Exercises"""

# 1
"""Welcome message to user which calls three functions and creates a welcome message to greet the user"""
while True:
    def name():
        answer = input('What is your name?')
        return answer
    def age():
        num = input('How old are you')
        return num
    def hobbies():
        hobs = input('What are your hobbies?')
        return hobs
    users_name = name()
    users_age = int(age())
    users_hobbies = hobbies()

    funny_message = 'You are very old! WOOOOOOOOOOOw'
    nice_message = 'You are very young'
    message = ''
    if users_age > 30:
        message = funny_message
    else:
        message = nice_message
    print(f'Hello, {users_name}. You are {users_age} {message}. My favorite hobbies are {users_hobbies} too! Lets go out.')



# 2
#Write a program that asks the user for a number then prints the following sentence that number of times:
# ‘I am back to check on my skills!’ If the number is greater than 10, print this sentence instead:
# ‘Python conditions and loops are a piece of cake.’ Assume you can only pass positive integers.


def number():
    num = input('Pick a number')
    return num

nums = int(number())
if nums > 10:
    print('Python conditions and loops are a piece of cake')
else:
    for x in range(nums):
        print('I am back to check on my skills!')


def n():
    ans= int(input('Pick a number'))
    return ans
ans= n()
if ans > 10:
    print('Python conditions and loops are a piece of cake')
else:
    if ans < 10:
        for x in range(ans):
            print('I am back to check on my skills!')