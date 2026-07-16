"""

Longest Repeating Character Replacement
level: Medium

You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
"""

from collections import defaultdict

def longest_repeating_character_replacement(s: str, k: int) -> int:
    left = 0
    max_length = 0
    max_count = 0
    char_count: dict[str, int] = defaultdict(int)

    for right in range(len(s)):
        char_count[s[right]] += 1
        max_count = max(max_count, char_count[s[right]])

        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length