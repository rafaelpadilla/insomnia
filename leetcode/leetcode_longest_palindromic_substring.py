# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.


def longestPalindrome2(s):
    len_s = len(s)
    anchor = 0
    left, right = anchor, anchor
    res = []
    res_len, length = 0, 1

    res = s[anchor]
    while anchor < len_s:
        left -= 1
        right += 1

        if left >= 0 and right < len(s):

            if s[left] == s[right]:
                length += 2
                continue

        if length > res_len:
            res_len = length
            res = s[anchor - abs(left):anchor + abs(right) - 1]
        anchor += 1
        right, left = anchor, anchor
        length = 1
    return res


def longestPalindrome(s):
    len_s = len(s)
    res = ''

    final_res = s[0] if len_s > 0 else ''

    for anchor in range(len_s):
        left = anchor - 1
        right = anchor + 1

        while right <= len_s - 1 and s[right] == s[anchor]:
            right = right + 1
            res = s[anchor:right]

        while left >= 0 and right <= len_s - 1 and s[left] == s[right]:
            res = s[left:right + 1]
            left = left - 1
            right = right + 1

        final_res = res if len(res) > len(final_res) else final_res

    return final_res


def test_func():
    test_cases = [{
        'input': 'babad',
        'output': 'bab'
    }, {
        'input': 'cbbd',
        'output': 'bb'
    }, {
        'input': 'a',
        'output': 'a'
    }, {
        'input': 'ac',
        'output': 'a'
    }, {
        'input': 'abcba',
        'output': 'abcba'
    }, {
        'input': 'ccc',
        'output': 'ccc'
    }, {
        'input': 'bb',
        'output': 'bb'
    }, {
        'input': 'ac',
        'output': 'a'
    }, {
        'input': '',
        'output': ''
    }]

    for test_case in test_cases:
        assert longestPalindrome(test_case['input']) == test_case['output']
