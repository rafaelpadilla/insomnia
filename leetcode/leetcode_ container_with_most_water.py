import numpy as np

def maxArea(height):
    index_height = np.argsort(height)

    # for h in height:

test_cases = {'input': [1,8,6,2,5,4,8,3,7], 'output': 49}

for _input, _output in test_cases.items():
    assert maxArea(_input) == _output