"""
Level: Medium
Longest Balanced Substring

You are given a string s consisting of lowercase English letters.
A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
Return the length of the longest balanced substring of s.

 

Example 1:

Input: s = "abccba"
Output: 6
Explanation: The entire string "abccba" is balanced because each distinct character appears the same number of times.
"abccba" has 2 'a's, 2 'b's, and 2 'c's. The length of the longest balanced substring is 6. 


Example 2:

Input: s = "cbbd"
Output: 2
Explanation: The substring "bb" is the longest balanced substring.
"bb" has 2 'b's. The length of the longest balanced substring is 2.
"""

from collections import defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        longest = 0
        for left in range(len(s)):
            max_freq = 0
            counter: dict[str, int] = defaultdict(int)

            for right in range(left, len(s)):
                char = s[right]
                counter[char] += 1

                if counter[char] > max_freq:
                    max_freq = counter[char]
                window_len = right - left + 1

                # Math trick: If max_freq * number of unique characters
                # equals the window length, then EVERY character must
                # have exactly max_freq occurrences.
                if max_freq * len(counter) == window_len:
                    if window_len > longest:
                        longest = window_len

        return longest
