"""Functions"""

# Definition: A function is a block of code that executes a specific task when it is called.
# You can pass arguments/ parameters through it.

# Example 1
"""Function that wishes the user a good night"""
def good_night(name = 'You.'):
    return 'Good night, ' + name

"""A default variable is passed through the function. When the function is called and a name is not passed through,
the default value 'You' will be used and the string 'Good night, You' returned."""

good_night()
'Good night, You.'

good_night(name='Pedro')
'Good night, Pedro'

good_night('Stacey')
'Good night, Stacey'

# Example 2
"""This function provides more flexibility but requires at least 1 argument to be passed through. 
The curly brackets {} are used as placeholders for different values to execute the function (string interpolation). The string method
 .format is used to configure the returned string which is cleaner and more presentable."""
def good_night_2(greetings, name= "you"):
    return '{}, {}'.format(greetings, name)

good_night_2('Sweet dreams')
'Sweet dreams, you'

good_night_2('Wassup my nigga', 'Terry')
'Wassup my nigga, Terry'

good_morning='Top of the morning to you!'
print(good_morning.format())
Top of the morning to you!

# Example 3

"""This function also provides greater flexibility as it is used to interporlate a string. F strings are used to pass through
different/ dynamic values in the {} placeholders"""
def good_morning_2(greeting, name="You", question='How was your sleep'):
    return f"{greeting}, {name}. Breakfast is ready. {question}?"

good_morning_2('Rise and shine', 'Bob')
'Rise and shine, Bob. Breakfast is ready. How was your sleep?'

