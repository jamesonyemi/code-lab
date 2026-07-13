"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

input: s = "abcabcbb"
output: 3

Explanation: The answer is "abc", with the length of 3.

input: s = "bbbbb"
output: 1

Explanation: The answer is "b", with the length of 1.

"""


from collections import defaultdict

def longest_substring_with_no_repeating_character(s: str) -> int:
    left = 0
    longest = 0
    counter: dict[str, int] = defaultdict(int)
    for right in range(len(s)):
        counter[s[right]] += 1
        while counter[s[right]] > 1:
            counter[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)

    return longest
 