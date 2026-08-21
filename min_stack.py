"""
Level: Medium
Question: Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the InventoryFloor class:
InventoryFloor() Initializes the object of the class.
void store(int val) Pushes the value val onto the top of the stack.
void removeLatest() Pops the value from the top of the stack.
int latest() Returns the value at the top of the stack.
int lowestStored() Returns the minimum value in the stack.

Example 1:
Input
["InventoryFloor", "store", "store", "store", "lowestStored", "removeLatest", "latest"]
[[], [1], [2], [3], [], [], []]

Output
[null, null, null, null, 1, null, 2]

Explanation
InventoryFloor inventoryFloor = new InventoryFloor();
inventoryFloor.store(1); // The stack is now [1]
inventoryFloor.store(2); // The stack is now [1, 2]
inventoryFloor.store(3); // The stack is now [1, 2, 3]
inventoryFloor.lowestStored(); // return 1, the minimum value in the stack
inventoryFloor.removeLatest(); // Remove the latest element from the stack [1, 2, 3]; we pop 3 from the stack. The stack is now [1, 2]
inventoryFloor.removeLatest(); // The stack is now [1, 2]
inventoryFloor.latest(); // return 2


Time Complexity: O(1) for each function.
Space Complexity: O(n)


Can you implement the InventoryFloor class using only one stack? If so, how would you do it?
Yes, it is possible to implement the InventoryFloor class using only one stack by storing pairs of values in the stack.
Each pair would consist of the actual value and the minimum value at that point in the stack. When pushing a new value,
we would compare it with the current minimum (which is stored in the top pair of the stack) and push a new pair with the new value and the updated minimum. When popping, we would simply pop the top pair, which would remove both the value and its corresponding minimum.

"""


from typing import Any, Dict, List, Optional


class Solution:
    def inventory_floor(self, commands: List[str], arguments: List[Any]) -> List[Any]:
        if len(commands) != len(arguments):
            raise ValueError("Commands and arguments must have the same length.")
        
        target = None
        result = []
        for command, call_arguments in zip(commands, arguments):
            if command == 'InventoryFloor':
                target = InventoryFloor(*call_arguments)
                result.append(None)
            else:
                result.append(getattr(target, command)(*call_arguments))
        return result


class InventoryFloor:
    def __init__(self):
        # implement
        self.stack = []
        self.min_stack = []

    def store(self, val: int) -> None:
        # implement
        self.stack.append(val)
        current_min = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(val, current_min))

    def removeLatest(self) -> None:
        # implement
        self.stack.pop()
        self.min_stack.pop()

    def latest(self) -> int:
        # implement
        return self.stack[-1]

    def lowestStored(self) -> int:
        # implement
        return self.min_stack[-1]