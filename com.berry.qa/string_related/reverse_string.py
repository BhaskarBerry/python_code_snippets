"""
-----------------------------------------------------------------
Reverse String using slice
-----------------------------------------------------------------
"""
text_str = "Bhaskar Berry"


def reverse_str(a):
    return a[:: -1]


"""
-----------------------------------------------------------------
Reverse String using inbuilt function 
-----------------------------------------------------------------
"""


def reverse_inbuilt(a):
    return "".join(reversed(a))


"""
-----------------------------------------------------------------
Reverse String using a loop
-----------------------------------------------------------------
"""


def reverse_loop(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1


"""
-----------------------------------------------------------------
Reverse String using recursion
-----------------------------------------------------------------
"""


def rev_recusion(s):
    if len(s) == 0:
        return s
    else:
        return rev_recusion(s[1:]) + s[0]


"""
-----------------------------------------------------------------
Reverse String using stack
-----------------------------------------------------------------
"""


def createStack():
    stack = []
    return stack


def size(stack):
    return len(stack)


def isEmpty(stack):
    if size(stack) == 0:
        return True


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


def reverse_stack(a):
    n = len(a)

    stack = createStack()

    for i in range(0, n, 1):
        push(stack, a[i])

    a = ""

    for i in range(0, n, 1):
        a += pop(stack)

    return a


# ----------------------------------------------------------------------------------------

print("The original string = ", text_str)
print("1st method reverse string using slice =", reverse_str(text_str))
print("2nd method reverse string using inbuilt funcction =", reverse_inbuilt(text_str))
print("3rd method reversed string (using loop): ", reverse_loop(text_str))
print("4th method reversed string (using recursion): ", rev_recusion(text_str))
print("5th method reversed string (using stack): ", reverse_str(text_str))
