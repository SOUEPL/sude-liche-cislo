# Do not edit these lines

import os.path
import sys


def test_existence():
    try:
        exists = os.path.exists("main.py")
        assert exists

    except FileNotFoundError:
        sys.exit(1)
