 # =========================
# how to read data
# input
# 4
# 4 5
# 00110
# 00011
# 11111
# 00000
# =========================

import sys
from xmlrpc.client import boolean

from sqlalchemy import false, true

visited = {}
trace = []
graph = []

# input
# round = int(sys.stdin.readline().rstrip())
# m, n = map(int, (x for x in sys.stdin.readline().rstrip().split()))

# for i in range(round):
#     ted = list(map(int, (x for x in sys.stdin.readline().rstrip())))
#     graph.append(ted)

m, n = 4, 5
graph=[[1,1,0,0,1],[1,0,1,1,0],[0,0,1,0,0],[1,1,0,1,1]]


# within a range
def able_togo(x,y) -> boolean:
    if(x>= 0 and x < m and y >= 0 and y < n):
         return True
    return False


def is_visited(x, y) -> boolean:
    if f"{x}{y}" not in visited:
        visited[f"{x}{y}"]= 1
        return True
    return False


def ted(x,y) -> int:
    if able_togo(x+1, y) and is_visited(x+1,y) and graph[x+1][y] == 1:
        ted(x+1,y)

    if able_togo(x, y+1) and is_visited(x,y+1) and graph[x][y+1] == 1:
        ted(x, y+1)

    if able_togo(x-1, y) and is_visited(x-1,y) and graph[x-1][y] == 1:
        ted(x-1,y)

    if able_togo(x, y-1) and is_visited(x,y-1) and graph[x][y-1] == 1:
        ted(x, y-1)
         
    return 1

def count_island() -> int:
    cnt_island = 0
    for x in range(m):
        for y in range(n):
            if graph[x][y] == 0:
                visited[f"{x}{y}"]= 1
                continue
            elif is_visited(x,y):
                cnt_island += ted(x,y)

            # print(visited)

    return cnt_island


print(f"Total island={count_island()}")