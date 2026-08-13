"""
A food delivery platform stores a driver's drop-off route as a one-way chain of stops. 
Each stop knows only which delivery came next when the driver originally headed outward from the kitchen. 
After a late-night traffic reroute, operations wants that chain rebuilt so dispatch can trace the path backward from the final customer to the restaurant.

You are given the first stop in this route record, and must rewire the chain so every stop points to the one that came before it instead. Return the new first stop of the rebuilt chain. The kitchen's menu ratings and a seasonal dumpling promotion are logged elsewhere, but they do not affect the route rewrite.

Some routes are empty, and some contain only a single delivery.

Constraints
The number of stops in order is in the range [0, 5000]
Each stop value in order is in the range [-5000, 5000]
order has type Optional[ListNode] and represents the first stop in a singly linked chain

Examples
1.order = [14, 27, 33, 48]→[48, 33, 27, 14]
The outward delivery chain is rewired so dispatch can start from the final stop and trace back toward the restaurant.

2.order = [9, 21]→[21, 9]
With two stops, each one simply ends up pointing to the other in the opposite direction.

3.order = [] → None
An empty route stays empty because there are no stop links to rewrite.

4.order = [5] → [5]
A single delivery stop is already both the start and end of the route, so the structure is unchanged.

5.order = [3, 8, 8, 12] → [12, 8, 8, 3]
Repeated stop values do not matter, because the route is reversed by rewiring links, not by comparing values.

Follow-up
Can you rebuild the route both by walking through the chain step by step and by letting the call stack unwind the rewiring for you?



Time complexity: O(n), where n is the number of stops in order. Each stop is visited once.
Space complexity: O(1), the algorithm does not use any additional data structures.
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"

    def __str__(self):
        return f"ListNode({self.val}, {self.next})"

    def _to_list(self):
        values = []
        current = self
        while current is not None:
            values.append(current.val)
            current = current.next
        return values

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        if isinstance(other, list):
            return self._to_list() == other
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result


def list_to_linked_list(values):
    head = None
    tail = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def rebuild_return_route(rebuild_return_route: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = rebuild_return_route
    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev

test_cases = [
    # Test case 1: Normal case with multiple stops
    ([14, 27, 33, 48], [48, 33, 27, 14]),
    # Test case 2: Single stop
    ([9, 21], [21, 9]),
    # Test case 3: Empty route
    ([], []),
    # Test case 4: Single delivery stop
    ([5], [5]),
    # Test case 5: Repeated stop values (should not matter)
    ([3, 8, 8, 12], [12, 8, 8, 3]),
]

for input_values, expected_output in test_cases:
    result = rebuild_return_route(None if not input_values else list_to_linked_list(input_values))
    if input_values:
        assert result == expected_output
    else:
        assert result is None

print("All test cases passed!")

