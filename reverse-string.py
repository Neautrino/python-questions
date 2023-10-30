'''
The question was sourced from a newsletter 
This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”

'''

def reverse_string(string):
    reversed_str = [i for i in string]
    rev_str = ""
    for i in range(len(reversed_str)):
        rev_str += reversed_str[(len(reversed_str)-1)-i]
    return rev_str
