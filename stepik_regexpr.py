import sys
import re

"""pattern = r'human'"""
"""replace = r'computer'"""


pattern = r'\b([aA]+)\b'
replace = r'argh'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, replace, line, count=1))



