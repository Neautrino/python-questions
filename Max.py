# The following is a function that can take any non-negative integer as an argument and return rearranged digits to create the highest possible number.

# Examples:

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def max_possible(n):
    a=[int(i) for i in str(n)]
    a.sort(reverse=True)
    return int("".join([str(i) for i in a]))