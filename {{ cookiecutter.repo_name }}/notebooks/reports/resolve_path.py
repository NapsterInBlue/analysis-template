'''
Adds your project to the PYTHONPATH environment variable,
allowing for project imports
'''

import sys as _sys
from pathlib import Path as _Path

_here = _Path(__file__).resolve()
_projectRoot = _here.parents[2]
_sys.path.insert(0, str(_projectRoot))
