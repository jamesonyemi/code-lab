"""
Level: Medium
Longest Balanced Substring

You are given a string s consisting of lowercase English letters.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abccba"
Output: 3
Explanation: The substring "abc" is the longest balanced substring.
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: The substring "bb" is the longest balanced substring.

"""

from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        # left = 0
        longest = 0

        for left in range(len(s)):
            max_freq = 0
            counter: dict[str, int] = defaultdict(int)

            for r in range(left, len(s)):
                char = s[r]
                counter[char] = counter.get(char, 0) + 1

                if counter[char] > max_freq:
                    max_freq = counter[char]
                window_len = r - left + 1

                # Math trick: If max_freq * number of unique characters
                # equals the window length, then EVERY character must
                # have exactly max_freq occurrences.
                if max_freq * len(counter) == window_len:
                    if window_len > longest:
                        longest = window_len

        return longest
