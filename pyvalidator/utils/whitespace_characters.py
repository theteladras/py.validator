import re
import sys

s = ''.join(chr(c) for c in range(sys.maxunicode + 1))

all_ws = ''.join(re.findall(r'\s', s))
