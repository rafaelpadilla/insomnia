# Reference: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/


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


test_cases = [{
    'inputs': {
        'numbers': [2, 7, 11, 15],
        'target': 9
    },
    'expected': (1, 2)
}, {
    'inputs': {
        'numbers': [2, 3, 4],
        'target': 6
    },
    'expected': (1, 3)
}, {
    'inputs': {
        'numbers': [-1, 0],
        'target': -1
    },
    'expected': (1, 2)
}]

for i, test_case in enumerate(test_cases):
    print(f'Test case {i+1}')
    # print(test_case)
    ret = twoSum_1(**test_case['inputs'])
    if ret == test_case['expected']:
        print('Passed')
    else:
        print('Failed!')
        print(f'Obtained: {ret} Expected: {test_case["expected"]}')
        break
