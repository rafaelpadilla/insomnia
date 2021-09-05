import os

import pytest

for file_name in os.listdir('.'):
    fp = os.path.join('.', file_name)
    if os.path.isfile(fp) and file_name.startswith('leetcode') and not file_name.startswith('TODO'):
        pytest.main([fp])
