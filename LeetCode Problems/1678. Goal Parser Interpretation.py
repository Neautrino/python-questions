class Solution:
    def interpret(self, command):
        result = ""
        i = 0
        while i < len(command):
            if command[i] == '(':
                if command[i + 1] == ')':
                    result += "o"
                    i += 2
                    continue
                result += "al"
                i += 4
                continue
            result += "G"
            i += 1
        return result
