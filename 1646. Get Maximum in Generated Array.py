#leetcode link https://leetcode.com/problems/get-maximum-in-generated-array
# using different types of solution 


# 1st one 
# Time Complexity O(n)
# Space Complexity O(n)
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        stack=[]
        for i in range(n+1):
            if i==0:
                stack.append(i)
            elif i==1:
                stack.append(i)
            else:
                if i%2==0:
                    stack.append(stack[i//2])
                else:
                    stack.append(stack[i//2]+stack[i//2+1])

        return max(stack)

# 2nd One 
# Time Complexity O(n^2)
# Space Complexity O(n^2)
# pure Recursion 
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        new=[0]*(n+1)
        def helper(n):
           
            if n==0:
                new[n]=0
                return 0
            elif n==1:
                new[n]=1
                return 1
            else:
                if n%2==0:
                    m=helper(n//2)
                    new[n]=m
                    return m
                else:
                    m=helper(n//2)+helper(n//2+1)
                    new[n]=m
                    return m
        for i in range(n+1):
            helper(i)
        return max(new)

# Time Complexity O(n^2)
# Space Complexity O(n^2)
# Recursion + Memoization
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        new=[0]*(n+1)
        def helper(n):
           
            if n==0:
                new[n]=(0)
                return 0
            elif n==1:
                new[n]=1
                return 1
            else:
                if n%2==0:
                    m=helper(n//2)
                    new[n]=m
                    return m
                else:
                    m=helper(n//2)+helper(n//2+1)
                    new[n]=m
                    return m
        for i in range(n+1):
            if new[i]==0:
                helper(i)
        return max(new)

# Time Complexity O(n)
# Space Complexity O(n)
# DP solution 
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        dp=[0]*(n+1)
        res=0
        dp[1]=1
        for i in range(2,n+1):
            if i%2==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=dp[i//2]+dp[i//2+1]
            res=max(dp[i],res)
        return res
