"""if statements"""

# Key words:
# Suite -- In Python, a suite is a block of code that consists of one or more statements.

# Definition: a conditional statement executes code which is dependent on the outcome.
# For example, "I will go for a walk if the weather is nice". This implies that you will
# not go for a walk if the weather is not nice.

# Conditional statements is a form of conditional structures as it controls the direction
# or flow of the arguments in a programme. This is referred to as a programme's conditonal flow. Such condtional statements
# require a compound statement or a block which are regarded as a single entity.

# When it is the target of an if statement, and <expr> is true, then all the statements in the block are executed.
# If <expr> is false, then none of them are (see below).

# True
destination = 'France'
if destination == 'France':
    print('conditional is True')

# False
destination = 'France'
if destination == 'Bali':
    print('conditional is True')

destination = 'France'
if destination == 'Bali':
    print('conditional is True')
print('conditional is False')


# For loop, if statement and or statement
numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

for num in numbers:
    if num.isalpha() or num == '7' or num == '3':
        print(num)
A
3
7
J
Q
K


# Else statements

# Else statements are used if you want to evaluate an alternative suite if the expression is false.
# If <expr> is true, the first suite is executed, and the second is skipped.
# However, if <expr> is false, the first suite is skipped and the second is executed.
# Either way, execution then resumes after the second suite. Both suites are defined by indentation.

x= 100
y= 200

if x == y:
    print('x is equivalent to y')
    print('this is correct')
else:
    print('x is not equivalent to y')
    print('this is incorrect')

x is not equivalent to y
this is incorrect

# Elif (else if) statements
# The elif statement is used if you need to evaluate an expression with multiple alternative suites.
# However, each elif statement that proceeds the if statement begins on a new line that is outside the if scope.
# If all elif statements are false, you can utiles an else statement. However, the else statement must only be used once
# and specified last.

# Example 1
hand_bag= 'Gucci'
if hand_bag=='Gucci':
    print('On Sale!')
elif hand_bag=='Chanel':
    print('Not on Sale.')
elif hand_bag=='Hermes':
    print('Not on Sale.')
elif hand_bag=='Bottega':
    print('Second Hand')
On Sale!

# Example 2
hand_bag= 'Bottega'
if hand_bag=='Gucci':
    print('On Sale!')
elif hand_bag=='Chanel':
    print('Not on Sale.')
elif hand_bag=='Hermes':
    print('Not on Sale.')
elif hand_bag=='Bottega':
    print('Second Hand')
Second Hand

# Example 3
hand_bag= 'Fendi'
if hand_bag=='Gucci':
    print('On Sale!')
elif hand_bag=='Chanel':
    print('Not on Sale.')
elif hand_bag=='Hermes':
    print('Not on Sale.')
elif hand_bag=='Bottega':
    print('Second Hand')
else:
    print('No stock')
No stock


# Note, it is also possible to write if conditional statements in one line by separating the expression
# and first statement with a colon, and separating proceeding statements with a semicolon. However, the expression has
# to be True for the code to be executed. Python gives semicolon precedence over colon. Therefore, the statements
# separated with a semicolon will be executed first as they are treated as a suite, and the expression last (see below).

a=10
b=5

# Truthy
if a>2: (print('this is True')); print('a is greater than 2')
this is True
a is greater than 2

# Falsy
if a<2: (print('this is True')); print('a is greater than 2')
# -- Result is a falsy value as a is not less than 2

# Truthy
if a==2: print('this is False'); print('a is not equivalent to 2')
elif a>2: print('this is True'); print('a is greater than 2')
else: print('this is False'); print('a is not less than 2')
this is True
a is greater than 2

# However, one-line conditional if statements are not encouraged as they are not easy to read.


"""Conditional Expressions"""
# A conditional expression, which is also called a ternary operator, allows you to execute an if else statement in one
# line of code. However, this is may not be easy to read for other software developers (see below).

# Example of conditional if statement
if clutch_bags > 10:
    print('There are multiple clutch bags in stock')
else:
    print('There are limited clutch bags in stock')

There are limited clutch bags in stock

# Example of conditional expression.
print('Hello.', ('There are multiples clutch bags in stock' if clutch_bags>10 else 'There are limited clutch bags in stock'))
Hello. There are limited clutch bags in stock


"""Python pass statement"""
# A pass statement can be used as a placeholder for a block of code that has not been implemented yet.
# Remember, python requires indentation. Therefore, when using an if statement, pass has to be indented for it
# to be executed. see below

if True:
    pass
print('Yes')
Yes

