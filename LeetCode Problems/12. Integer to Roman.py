# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.  Given an integer, convert it to a roman numeral.
# Question Link: https://leetcode.com/problems/integer-to-roman/
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s:
            current_value = roman_values[char]

            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

        return total
