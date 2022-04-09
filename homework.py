# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(*args):
    return max([*args])
            
# print(max_num(3,12,4))
# print(max_num(1,44,72))
    

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(a,b,c):
    return sum([a*b*c])

# print(mult_list(1,2,3))
# print(mult_list(2,3,4))


# Write a Python function called rev_string() to reverse a string.

def rev_str(x):
    return x[::-1]

# print(rev_str("hello"))
# print(rev_str(""))
# print(rev_str("meow meow"))

# Write a Python function called num_within() to check whether a number falls in a given range.
#   The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#   Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(i,a,b):
    return i in range(a,b+1)

# print(num_within(2,3,4))
# print(num_within(3,2,4))
# print(num_within(2,1,4))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#   The function accepts the number n, the number of rows to print
#   Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. 
#   Each number is the two numbers above it added together.

def pascal(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[1+r for l, r in zip(trow+y, y+trow)]
    return n>=1

print(pascal(6))