def number():
    num = input('Pick a number')
    return num


nums = int(number())

if nums > 10:
    print('Python conditions and loops are a piece of cake')
else:
    for x in range(nums):
        print('I am back to check on my skills!')

