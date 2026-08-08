"""
In a competitive arena, each match in a streak applies the same rating multiplier to a player's standing. Tournament tools need a reliable way to predict the final multiplier after many repeated matches, including recovery scenarios where a negative streak count means reversing the effect of earlier boosts.

Given a base arena multiplier and an integer streak length, compute the resulting combined multiplier after applying that same effect repeatedly. If the streak length is negative, treat it as the inverse of applying the positive streak.

Your result should be accurate for ordinary floating point calculations and efficient even when the streak length is very large.

Constraints
-100.0 < arena_multiplier < 100.0
-2^31 <= streak_count <= 2^31 - 1
streak_count is an integer
Either arena_multiplier != 0.0 or streak_count > 0
-10^4 <= result <= 10^4
The result is arena_multiplier raised to the power streak_count: compute arena_multiplier ^ streak_count, where x^0 = 1 and x^-n = 1 / x^n. Because streak_count may be as low as -2^31, compute the magnitude of the exponent in a width that holds 2^31 (do not negate a 32-bit integer, which would overflow). An answer is accepted when it is within a relative tolerance of 1e-9 of the reference value: |your_result - expected| <= 1e-9 * max(1.0, |your_result|, |expected|).

Examples
1.arena_multiplier = -1.0, streak_count = -2147483648 → 1.0
Verified against the canonical solution as case-027.

2.arena_multiplier = 3.0, streak_count = 0 → 1
Verified against the canonical solution as case-001.

3.arena_multiplier = -1.0, streak_count = 2147483647 → -1.0
Verified against the canonical solution as case-015.

4.arena_multiplier = 10.0, streak_count = -3 → 0.001
Verified against the canonical solution as case-002.

5.arena_multiplier = 5.0, streak_count = 1 → 5.0
Verified against the canonical solution as case-003.


Follow-up
Can you compute the final multiplier without repeating the same multiplication once per match in the streak?

Time Complexity: O(log n)
Space Complexity: O(1)

"""

class Solution:
    def compute_streak_multiplier(self, arena_multiplier: float, streak_count: int) -> float:
        if streak_count == 0:
            return 1.0

        is_negative = streak_count < 0
        magnitude =  abs(streak_count)

        result = 1.0
        base =  arena_multiplier  

        while magnitude > 0:
            if magnitude & 1:  # bitwise check for odd/even
                result *= base
            base *=base

            magnitude >>=1  # Fast bitwise right-shift

        if is_negative:
            if result == 0.0:
                return float('inf')
            return 1.0/result

        return result                