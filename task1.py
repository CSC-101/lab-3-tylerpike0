

more = [x + 1 for x in [1,2,3,4]]     # List, in order, the values that x takes at each step. x = 1, 2, 3, 4
print()                               # What is the value of more at this point? more = [2, 3, 4, 5]

##############################################
def square(n:int) -> int:
    return n * n                           # Record, in order of the calls, each value of n and      n = 1, 2, 3, 4
                                           # the corresponding return value.                         return 1, 4, 9, 16


squares = [square(x) for x in [1,2,3,4]]   # What is the value of squares and how does this relate to the
print()                                    # values recorded above?     squares = [1, 4, 9, 16] which is a list of the values returned above

##################################################

def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and    n = 0, 1, 2, 3, 4
                                             # the corresponding return value.    return False, False, False, True, True


answer = [x for x in range(5) if check(x)]   # What is the value of answer?   Answer = [3, 4]
print()

#######################################################

def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and  m = 3, 4
                                             # the corresponding return value.


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and   n = 0, 1, 2, 3, 4
                                             # the corresponding return value.    return False, False, False, True, True


answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer?   answer = [4, 5]
print()

#######################################################