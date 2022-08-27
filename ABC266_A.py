import io
import sys

_INPUT = """\
6
atcoder
a
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  print(S[len(S)//2])