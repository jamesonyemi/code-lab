"""
# Sliding Window Technique

Longest Substring Without Repeating Characters
level: Medium

Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1
"""

def longest_substring_without_repeating_characters(s: str) -> int:
    left = 0
    longest = 0
    window = set()
    
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        longest = max(longest, right - left + 1)
    
    return longest    