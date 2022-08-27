import io
import sys

_INPUT = """\
6
0 0
1 0
1 1
0 1
0 0
1 1
-1 0
1 -1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A=[list(map(int,input().split())) for _ in range(4)]
  ans='Yes'
  if ((A[1][1]-A[0][1])*(A[2][0]-A[0][0])-(A[1][0]-A[0][0])*(A[2][1]-A[0][1]))*((A[3][1]-A[0][1])*(A[2][0]-A[0][0])-(A[3][0]-A[0][0])*(A[2][1]-A[0][1]))>0: ans='No'
  if ((A[0][1]-A[1][1])*(A[3][0]-A[1][0])-(A[0][0]-A[1][0])*(A[3][1]-A[1][1]))*((A[2][1]-A[1][1])*(A[3][0]-A[1][0])-(A[2][0]-A[1][0])*(A[3][1]-A[1][1]))>0: ans='No'
  print(ans)