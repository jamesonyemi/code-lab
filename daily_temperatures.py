
from collections import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] <= t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
            
        while stack:
            j = stack.pop()
            ans[j] = 0
            
        return ans    