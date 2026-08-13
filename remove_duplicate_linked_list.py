"""
A maintenance tool receives a release chain whose records are ordered by build rank. 
Each record points to the next record, and 
the chain may contain repeated ranks when several deployments share the same build.

The tool must keep the first record for each rank and reconnect the chain so every retained record leads to the next higher rank. It should return the original entry point when one exists, or an empty result when the chain has no records.

The input can be empty or contain up to 300 records, with ranks already ordered low to high. Cleanup should reuse existing records rather than create replacements.

Constraints
The number of records in release_chain is between 0 and 300.
Each build rank is between -100 and 100.
release_chain is ordered in ascending build-rank order.
Existing release records should be reused.

Examples
1.release_chain = [4, 4, 9] → [4, 9]
The second record with build rank 4 is bypassed, leaving the first 4 followed by 9.

2.release_chain = [2, 5, 5, 8, 8, 8] → [2, 5, 8]
Only the first record for each ordered build rank remains in the chain.

3.release_chain = [] → None
There are no release records, so the returned entry point is empty.

4.release_chain = [7] → [7]
A single release record has no later record to remove.

5.release_chain = [3, 3, 3, 3] → [3]
All records share one build rank, so the first record is retained and the rest are unlinked.


Time complexity: O(n), where n is the number of records in release_chain. Each record is visited once.
Space complexity: O(1), the algorithm does not use any additional data structures.

"""


from typing import Any, Dict, List, Optional


class Solution:
    def clean_release_chain(self, release_chain: Optional["ListNode"]) -> Optional["ListNode"]:
        if release_chain is None:
            return None

        current = release_chain
        while current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return release_chain
    
