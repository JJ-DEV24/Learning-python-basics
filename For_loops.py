# For loops

# How to find indices in a list using a for loop
ten_times_table=[]
indices_of_interest=[370,650,780]
for x in range(0,1000,10):
    ten_times_table.append(x)

for each in indices_of_interest:
    print(ten_times_table.index(each))

# Nested for loops:

# 1. The first loop (parent loop) will go over the second loop (child loop) one by one.
fresh=['Fresh']
fruits=['apples', 'mangoes', 'pears', 'pineapples', 'strawberries', 'cherries', 'bananas', 'dragon fruit', 'kiwi', 'red grapes', 'white grapes']
for Fresh in fresh:
    for fruit in fruits:
        fresh_fruit= Fresh + ' ' + fruit
        print(fresh_fruit)


# 2.
# (Homework for maths class)
three_times_tables=[3, 6, 9, 12, 15]
multiplied_by_two=[2=]
for num in three_times_tables:
    for times in multiplied_by_two:
        answer= num + times
        print(answer)

# 3.
'''
questions=[]
for num in three_times_tables:
    question=[num,'*','2','=']
    questions.append(question)
    print(questions)
    
for each in questions:
    answer= int(each[0]) * int(each[2])
'''
###

for year in years:
    for month in months:
        for day in days:
            Date= day + ' ' + month + ' ' + year
            print(Date)

# 3. --> review for loops using range and formatted strings to code ('1,1','1,2','1,3') etc
for x in range(1, 11):
    for y in range(1, 10):
        nums  ???
        print(nums)


def hello():
    print('hello')

for x in range(0,201):
    hello()




def hello_person(name):
        print('Hello ' + name)

hello_person('asdfghjhgfdsdfghjhgfdsdcvfghngbvfdsxxdcvfg')