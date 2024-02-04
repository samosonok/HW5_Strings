import keyword
import string
# The user enters a string. Your task is to check if this string can be a variable name.
#
# A variable name cannot:
# - start with a digit,
# - consist only of digits,
# - contain uppercase letters, spaces, and punctuation marks (except for the underscore "_").
# - be any of the reserved words.
# - however, a variable name can consist of only one underscore "_".
#
# The list of reserved words can be taken from keyword.kwlist.
# As a result of the check, print True if the variable name is permissible or False if not.
# Examples of variable names and the result of the check (=> do not need to be printed):
# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True

user_input = str(input("Please enter variable name: "))

result = True
punctuation_chars = set(string.punctuation) - set('_')
if (user_input[0].isdigit() or
        user_input.isdigit() or
        user_input in keyword.kwlist or
        any(char.isupper() or char.isspace() for char in user_input) or
        any(char in punctuation_chars for char in user_input)):
    result = False

print(result)
