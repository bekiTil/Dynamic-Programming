# Time Complexity O(n)
# Space Complexity O(1)
# dp soluiton finding the right answer
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n<=2:
            return 1
        num1=0
        num2=1
        num3=1     
        
        for i in range(2,n):
            num=num1+num2+num3
            num3,num2,num1=num,num3,num2
        return num