import io
import sys

_INPUT = """\
6
998244354
-9982443534
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N=int(input())
  print((N-mod)%mod)