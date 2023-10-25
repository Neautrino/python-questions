class Solution:
    def isHappy(self, n):
        for j in range(7):
            str_n = str(n)
            sum = 0
            for i in range(len(str_n)):
                sum += int(str_n[i]) ** 2
            
            if sum == 1:
                return True
            
            n = sum
        
        return False
