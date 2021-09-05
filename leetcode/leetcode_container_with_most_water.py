# https://leetcode.com/problems/container-with-most-water/

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.


def maxArea(height):
    # Inicia po primeiro e o último
    i_l, i_r = 0, len(height) - 1
    max_area = 0

    while i_l < i_r:
        max_area = max(max_area, (i_r - i_l) * min(height[i_l], height[i_r]))
        # move para direita
        if height[i_l] < height[i_r]:
            i_l += 1
        else:
            i_r -= 1
    return max_area


def test_func():
    test_cases = [{
        'input': [1, 8, 6, 2, 5, 4, 8, 3, 7],
        'output': 49
    }, {
        'input': [1, 1],
        'output': 1
    }, {
        'input': [4, 3, 2, 1, 4],
        'output': 16
    }, {
        'input': [1, 2, 1],
        'output': 2
    }]

    for test_case in test_cases:
        assert maxArea(test_case['input']) == test_case['output']
