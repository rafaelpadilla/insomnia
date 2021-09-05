# Reference: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.


def twoSum_1(numbers, target):
    # Create a dictionary to store differences between target and element
    # difference=target-element
    # where key=>difference and value=>index+1
    # Given numbers=[2,7.11.15] and target=9 dict = {7:1, 2:2, -2:3, -6:4}
    diff_indexes = {}
    # Loop through indexes
    for i, element in enumerate(numbers):
        # Check if element is the difference computed before
        if element in diff_indexes:
            # Return index of the difference and current index
            return (diff_indexes[element], i + 1)
        # Compute the difference
        diff = target - element
        # Store the difference as the key
        diff_indexes[diff] = i + 1
    # PYTHON 3
    # Runtime: 64 ms, faster than 63.82% of Python3 online submissions for Two Sum II - Input array is sorted.
    # Memory Usage: 14.8 MB, less than 33.51% of Python3 online submissions for Two Sum II - Input array is sorted.
    #
    # PYTHON
    # Runtime: 44 ms, faster than 80.84% of Python online submissions for Two Sum II - Input array is sorted.
    # Memory Usage: 13.6 MB, less than 67.40% of Python online submissions for Two Sum II - Input array is sorted.


def twoSum_2(numbers, target):
    # Create a dictionary to store differences between target and element
    # difference=target-element
    # where key=>difference and value=>index+1
    # Given numbers=[2,7.11.15] and target=9 dict = {7:1, 2:2, -2:3, -6:4}
    diff_indexes = {}
    # Loop through indexes
    for i in range(len(numbers)):
        # Check if element is the difference computed before
        if numbers[i] in diff_indexes:
            # Return index of the difference and current index
            return (diff_indexes[numbers[i]], i + 1)
        # Compute the difference
        diff = target - numbers[i]
        # Store the difference as the key
        diff_indexes[diff] = i + 1
    # PYTHON 3
    # Runtime: 64 ms, faster than 63.82% of Python3 online submissions for Two Sum II - Input array is sorted.
    # Memory Usage: 14.6 MB, less than 86.52% of Python3 online submissions for Two Sum II - Input array is sorted.
    #
    # PYTHON
    # Runtime: 36 ms, faster than 99.38% of Python online submissions for Two Sum II - Input array is sorted.
    # Memory Usage: 14.4 MB, less than 12.53% of Python online submissions for Two Sum II - Input array is sorted.


def test_func():
    test_cases = [{
        'input': {
            'numbers': [2, 7, 11, 15],
            'target': 9
        },
        'output': (1, 2)
    }, {
        'input': {
            'numbers': [2, 3, 4],
            'target': 6
        },
        'output': (1, 3)
    }, {
        'input': {
            'numbers': [-1, 0],
            'target': -1
        },
        'output': (1, 2)
    }]

    for test_case in test_cases:
        assert twoSum_2(**test_case['input']) == test_case['output']
