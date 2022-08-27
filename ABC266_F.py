import io
import sys

_INPUT = """\
6
5
1 2
2 3
1 3
1 4
2 5
3
1 2
1 4
1 5
10
3 5
5 7
4 8
2 9
1 2
7 9
1 6
4 10
2 5
2 10
10
1 8
6 9
8 10
6 8
3 10
3 9
1 10
5 8
1 10
7 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class UnionFind():
    def __init__(self, n):
      self.n = n
      self.parents = [-1] * n
    def find(self, x):
      if self.parents[x] < 0:
        return x
      else:
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self, x, y):
      x = self.find(x)
      y = self.find(y)
      if x == y:
        return
      if self.parents[x] > self.parents[y]:
        x, y = y, x
      self.parents[x] += self.parents[y]
      self.parents[y] = x
    def size(self, x):
      return -self.parents[self.find(x)]
    def same(self, x, y):
      return self.find(x) == self.find(y)
    def members(self, x):
      root = self.find(x)
      return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
      return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
      return len(self.roots())
    def all_group_members(self):
      return {r: self.members(r) for r in self.roots()}
    def __str__(self):
      return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

  from collections import deque
  def bfs(G,s):
    parent=[-1]*N
    inf=10**6
    D=[inf]*len(G)
    D[s]=0
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if D[y]>D[x]+1:
          parent[y]=x
          D[y]=D[x]+1
          dq.append(y)
    return D,parent

  def bfs2(G,s):
    inf=10**6
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if parent[x]!=y:
          parent[y]=x
          dq.append(y)
          used[y]=0
          idx[y]=tmp

  N=int(input())
  G=[set() for _ in range(N)]
  uf=UnionFind(N)
  for _ in range(N):
    u,v=map(lambda x: int(x)-1,input().split())
    if uf.find(u)!=uf.find(v):
      G[u].add(v)
      G[v].add(u)
      uf.union(u,v)
    else:
      x,y=u,v
  depth, parent=bfs(G,0)
  cycle=deque([x,y])
  while depth[x]>depth[y]:
    x=parent[x]
    cycle.appendleft(x)
  while depth[y]>depth[x]:
    y=parent[y]
    cycle.append(y)
  while x!=y:
    x=parent[x]
    y=parent[y]
    cycle.appendleft(x)
    cycle.append(y)
  for i in range(len(cycle)-1):
    u,v=cycle[i],cycle[i+1]
    if v in G[u]: G[u].remove(v)
    if u in G[v]: G[v].remove(u)
  used=[-1]*N
  idx=[-1]*N
  tmp=0
  for i in range(N):
    if used[i]==0: continue
    used[i]=0
    idx[i]=tmp
    bfs2(G,i)
    tmp+=1
  Q=int(input())
  for _ in range(Q):
    x,y=map(lambda x: int(x)-1,input().split())
    if idx[x]==idx[y]: print('Yes')
    else: print('No')