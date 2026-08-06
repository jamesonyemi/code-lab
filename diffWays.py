"""
A playlist editor encodes a mix cue as a string expression containing non-negative integers 
and the operators +, -, and *. 
Every valid way to fully parenthesize the expression corresponds to a different order 
in which the mix cue operations are applied, potentially yielding a different final score. 

Given the expression string, return the score produced by every valid full parenthesization of the expression — one result per parenthesization, including duplicates when two different parenthesizations happen to yield the same score. Do not remove duplicate values. Results may be returned in any order.

Constraints
1 <= expression.length <= 20
Each integer token in the expression is between 0 and 99 inclusive
The expression contains only non-negative integers and the operators +, -, and *
Results may be returned in any order
Examples
1.expression = '2-1-1' → [2, 0]
There are two full parenthesizations: (2-(1-1)) = 2-0 = 2 and ((2-1)-1) = 1-1 = 0. 
One result is listed per parenthesization, giving [2, 0].

2.expression = '2*3-4*5' → [-34, -10, -14, -10, 10]
The five full parenthesizations evaluate to: 
(2*(3-(4*5))) = -34, (2*((3-4)*5)) = -10, 
((2*3)-(4*5)) = -14, ((2*(3-4))*5) = -10, 
and (((2*3)-4)*5) = 10. 
The value -10 is produced by two different parenthesizations and both copies are kept — the answer lists one score per parenthesization rather than a deduplicated set: [-34, -10, -14, -10, 10].

3.expression = '0' → [0]
The expression has no operator, so there is a single parenthesization (the integer itself), 
giving the one-element list [0].

4.expression = '2-1-1' → [2, 0]
There are two full parenthesizations: 
(2-(1-1)) = 2-0 = 2 
and ((2-1)-1) = 1-1 = 0. 
One result is listed per parenthesization, giving [2, 0].

5.expression = '2' → [2]
A lone integer admits exactly one parenthesization, so the result is the one-element list [2].

Follow-up
Could you use memoization to avoid recomputing subexpressions 
that appear more than once in the recursion tree?
"""

"""
Level: Medium
"""


from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def solve(start: int, end: int)-> List[int]:
            # Return Cache if the subsegment was already computed
            if (start, end) in memo:
                return memo[(start, end)]
            result = []
            isNumber = True # base case

            # we loop via the current window via the indices
            for i in range(start, end + 1):
                op = expression[i]
                if op in "+-*":
                    isNumber = False
                    """
                    Divide: Solve left and right segments with index
                    range
                    """

                    left = solve(start, i - 1)
                    right = solve(i+1, end)

                    """
                    Conquer: Combine both result found
                    """
                    for l in left:
                        for r in right:
                            if op == "+": result.append(l + r)
                            elif op == "-": result.append(l - r)
                            else: result.append(l * r)
            """
            Base Case: if no operator is found, 
            parse string as a number    
            """
            if isNumber:
                num = 0
                for i in range(start, end + 1):
                    num = num * 10 + int((expression[i]))
                result.append(num)     

            memo[(start, end)] = result
            return result   

        return solve(0, len(expression) - 1)        

