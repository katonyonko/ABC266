import io
import sys

_INPUT = """\
6
3
1 0 100
3 3 10
5 4 1
3
1 4 1
2 4 1
3 4 1
10
1 4 602436426
2 1 623690081
3 3 262703497
4 4 628894325
5 3 450968417
6 1 161735902
7 1 707723857
8 2 802329211
9 0 317063340
10 2 125660016
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  dp=[[-1]*5 for _ in range(10**5+1)]
  dp[0][0]=0
  snuke=[list(map(int,input().split())) for _ in range(N)]
  now=0
  for i in range(10**5):
    for j in range(5):
      dp[i+1][j]=max(dp[i+1][j],dp[i][j])
      if j>0: dp[i+1][j]=max(dp[i+1][j],dp[i][j-1])
      if j<4: dp[i+1][j]=max(dp[i+1][j],dp[i][j+1])
      if now<N and snuke[now][0]==i+1 and snuke[now][1]==j and dp[i+1][j]>=0:
        dp[i+1][j]+=snuke[now][2]
    if now<N and snuke[now][0]==i+1:
      now+=1
  print(max(dp[-1]))