"""f strings"""

# Example 1
def jeans(size, style):
    stock= 10
    new_stock= stock//2
    return f'{new_stock} {size} {style}'


# Example 2
def last_name_adder(first_name, extended_name):
    answer = 5 + 10
    new_answer = answer * 2
    names = first_name + ' ' + extended_name
    return f'{names} {new_answer}'

# Example 3
"""This function also provides greater flexibility as it is used to interporlate a string. F strings are used to pass through
different/ dynamic values in the {} placeholders"""
def good_morning_2(greeting, name="You", question='How was your sleep'):
    return f"{greeting}, {name}. Breakfast is ready. {question}?"

good_morning_2('Rise and shine', 'Bob')
'Rise and shine, Bob. Breakfast is ready. How was your sleep?'


