"""
A social platform archives tiny moderation logs that describe members stepping into and out of temporary spaces such as circles, watch rooms, and project hubs. Each symbol in a log marks either an entry token or an exit token for one specific space type.

Trust and safety wants to reject malformed logs before they reach analytics. A log is acceptable only if every exit matches the most recent still-open entry of the same space type, and nothing exits before its matching entry appears. Some moderators like to annotate incidents with lunar phase notes, but those notes are stored elsewhere and do not affect validation. The three space types happen to use different token shapes because of an old design experiment from the platform's early mobile era.

Constraints
1 <= activity_log.length <= 10^4
activity_log consists only of the six characters '(', ')', '[', ']', '{', '}'
Return a boolean indicating whether the full activity_log is structurally acceptable

Examples
1. activity_log = "((((((()))))))" → True
2. activity_log = "{[()]}" → True
Several nested spaces are opened and closed in perfectly consistent order.

3. activity_log = "[[[[[[{{{{}}}}]]]]]]" → True
4. activity_log = "({[(])})" → False
5. activity_log = "([)]" → False
The exit sequence tries to leave an older space before leaving the most recently entered one.

Follow-up
Could you validate the log in one left-to-right pass while using memory proportional only to the number of currently unmatched entries?

Time Complexity: O(n)
Space Complexity: O(n)

"""

class Solution:
    def is_valid_activity_log(self, activity_log: str) -> bool:
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        for char in activity_log:
            if char in "([{":
                stack.append(char)
            elif char in pair: 
                if not stack or stack[-1] != pair[char]:
                    return False   
                stack.pop()
            
        return len(stack) == 0        