# Operators are used to perform an operation/ action on values or variables which are called operands.

# There are various operators in Python:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


"""Logical operators"""
# Logical operators are used in conditional statements which result in either True or False.
# These are 'logical' and, 'logical' or, 'logical' not. See below examples using if (conditional) statements.

# 'logical' and --
a=10
b=5

# Example 1
if a and b:
    print('yes')
else:
    print('no')
yes ('yes' printed as both a and b are present)

# Example 2
if a>2 and b>2:
    print('yes')
else:
    print('no')
yes ('yes' printed as both arguments are required to be True.)

# Example 3
"""Complete this example using elimination"""
Year=0
year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
how many times does 4 go into 0? 0
0 == 0 and (year % 100 != 0 or year % 400 == 0))
0 == 0 = True
True and (year % 100 != 0 or year % 400 == 0))
# How many times does 100 go into 0 = 0
True and (0 != 0 or year % 400 == 0))
True and (False or year % 400 == 0))
True and (False or 0 == 0))
True and (False or True)
True and True
Answer = True

# 'logical' or --
a=10
b=5

if a>2 or b<2:
    print('yes')
else:
    print('no')
yes ('yes' printed as at least one of the arguments has to be True.)


# 'logical' not --
a=10
b=5

if not (a > 2 and b > 2):
    print('yes')
else:
    print('no')

no ('no' printed as the not operator reverses the result if it is True. Therefore, result is False.)


"""Comparison Operators"""
# Comparison operators are used to compares two values.

==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
