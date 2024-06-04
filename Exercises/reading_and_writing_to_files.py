""" File Objects """

# To read or write to a file, you must use the open() and pass in the parameter to set the mode of the file:
#       'w' = creates (write) a new file. Overrides existing file
#       'r' = read a file, Error if the file does not exist.
#       'r+' = read and write to a file. Creates a new file if it does not exist.
#       'a' = append to an existing file at the very end. Creates a new file if it does not exist
#       'x' = create a new file

# Additionally, you can specify if the file should be handles in text or binary mode:
#       't' = text mode.
#       'b' = binary mode which is used specifically for images.

# To delete a file, you have to import the Operating System (OS) module:
# syntax:
#           import os

# Check if the file exists first to avoid getting an error:
#            if os.path.exists('file_name.txt'):
#               os.remove('file_name.txt')
#            else:
#               print('The file does not exist')

# To delete an entire folder, use the os.rmdir() method:
#             Import os
#             os.rmdir('my_folder')


# It is advisable to use a context manager (an object used to manage resources such as file handling,
# network connections and database connections).

# See example of context manager being used to write a new file below...

'''Write a new file'''
with open('cyprus_itinerary.text', 'w') as f:
    f.write('Hello, handsome! I have compiled an extensive list of activities that I thought would be exhilarating, for'
            ' days when we went to chase the thrill and adrenaline rush, and calming, should we decide to rest and'
            ' vegetate :) /n' 'Please feel free to append to the list, and highlight any existing activities you '
            'are not keen to experience xx')

# This context manager automatically closes the file once the code has been run. Therefore, you need deal with the
# context of this file from within the context manager.

'''Read a file'''
# with open('cyprus_itinerary.text', 'r') as f:
#     f_content = f.read()
#     print(f_content)

# Note, read() method returns the number of bytes to return. Therefore, it is beneficial to do:

with open('cyprus_itinerary.text', 'r') as f:
    for line in f:
        print(line, end='')
# The above code ensures it gets 1 line at time instead of all at once. This is more efficient and saves memory.

'''Read a large file'''
# You can use a while loop to iterate over the characters in a large file. See below...

with open('Card_game_v2.py', 'r') as f:
    size_to_read = 100
    f_content = f.read(size_to_read)
    while len(f_content) > 0:
      print(f_content, end='')
      f_content = f.read(size_to_read)

# Line 60 = created a variable that contains number of characters that you want to iterate over

# Line 61 = created a variable that contains the number of characters you want to iterate over which is has been passed
# through the read() method. This method takes that number and "reads" the first total amount of characters that you
# stored in the size_to_read_variable. This is then saved in the variable f_content.

# Line 62 = used a while loop to ensure that while the length of f_content is greater than 0, (line 63) print the
# content.

# Line 64 is CRUCIAL as you will have an infinite loop without it. Therefore, line 64 will print an empty string once
# the last character has been iterated over. The print statement on this line does not meet the while conditional. Thus,
# the conditional will cease to be executed.

