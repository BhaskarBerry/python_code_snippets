"""
Reverse Integer
# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.
"""


def reverse_int(a):
    string = str(a)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])


inp = input("Enter the integer : ")
print("The input number is :", inp)
print("The reverse number is : ", reverse_int(inp))
