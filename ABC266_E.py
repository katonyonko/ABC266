import io
import sys

_INPUT = """\
6
1
2
10
100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  dp=[[0]*6 for _ in range(N)]
  for i in range(6):
    dp[0][i]=i+1
  for i in range(N-1):
    s=sum(dp[i])
    d=s//pow(6,i+1)
    for j in range(6):
      if j<d: dp[i+1][j]=s
      else: dp[i+1][j]=(j+1)*pow(6,i+1)
  print(sum(dp[-1])/pow(6,N))