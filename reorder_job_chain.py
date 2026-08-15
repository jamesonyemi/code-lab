"""
An internal release system stores deployment jobs as a singly connected chain. Each job points to the next job scheduled for the same release, and the chain must remain intact so the runner can visit every job exactly once.

A maintenance request identifies two positions, start_slot and end_slot. Reverse the order of the jobs occupying those positions, while leaving every job before and after that range in its original place. Return the updated chain's first job.

The release may contain only one job, and the requested range can cover the entire chain or a single position. No job should be duplicated or lost.

Constraints
1 <= number of jobs in chain <= 500
-500 <= job priority value <= 500
1 <= start_slot <= end_slot <= number of jobs in chain

Examples

1.chain_start = [12, 18, 25, 31, 44], start_slot = 2, end_slot = 4
→[12, 31, 25, 18, 44]
The jobs in positions 2 through 4 change from 18, 25, 31 to 31, 25, 18, while the first and last jobs stay in place.

2.chain_start = [73], start_slot = 1, end_slot = 1
→ [73]
A one-job release has no ordering change when its only position is selected.

3.
chain_start = [4, 9, 15, 22], start_slot = 1, end_slot = 3
→[15, 9, 4, 22]
The first three jobs are reversed, and the fourth job remains at the end.

4.chain_start = [6, 11, 17, 23], start_slot = 2, end_slot = 4
→[6, 23, 17, 11]
The suffix beginning at the second job is reversed without moving the initial job.

5.chain_start = [8, 14, 19, 27, 35], start_slot = 1, end_slot = 5
→[35, 27, 19, 14, 8]
The requested range covers the complete release chain, so every job changes order.

Follow-up
Can the chain be updated while making only one forward visit through its jobs?

Time complexity: O(n), where n is the number of jobs in chain. Each job is visited once.
Space complexity: O(1), the algorithm does not use any additional data structures.
"""


from typing import Any, Dict, List, Optional
class Solution:
    def reorder_job_chain(self, chain_start: Optional["ListNode"], start_slot: int, end_slot: int) -> Optional["ListNode"]:
        # implement
        if chain_start is None or start_slot >= end_slot: return chain_start

        dummy = ListNode(0)
        dummy.next = chain_start

        prev_start = dummy

        for _ in range(start_slot - 1):
            prev_start =  prev_start.next

        prev = None
        cur = prev_start.next

        tail_segment = cur

        for _ in range(end_slot - start_slot + 1):
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        prev_start.next = prev
        tail_segment.next   = cur

        return dummy.next

