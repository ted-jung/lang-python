import sys
import bisect
import heapq

from collections import Counter


# =========================
# how to read data
# input
# 4
# 00110
# 00011
# 11111
# 00000
# =========================

pg = []
round = int(sys.stdin.readline())
for i in range(round):
    pg.append(list(map(int, (i for i in sys.stdin.readline().rstrip()))))
print(pg)


# input-graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


print(dir(__builtins__))

for i in dir(__builtins__):
    print(i)

print(" ted in gj   =  ".strip())
print("->".join(" ted in gj   =  ".split()))
print(list("".join(" ted in gj".strip())))
print(len(list(" ted in gj")))

for i in list(" haha ted"):
    print(i)

print(Counter(list("teed haha hope".strip())))
print("--".join(" haha haha".split()))

# =========================
# reverse a string
# =========================
def reversed_string_heapq(ted:str) -> str:

    pq = []
    temp = ""

    for i in range(len(ted)):
        heapq.heappush(pq,(len(ted)-1-i,ted[i:i+1]))

    for i in range(len(ted)):
        temp+=heapq.heappop(pq)[1]

    return temp

# =========================
# list를 스택처럼 (FIFO)
# =========================
def reversed_string_list(ted:str) -> str:
    stack = []

    for i in range(len(ted)):
        stack.append(ted[i:i+1])

    temp=""
    for i in range(len(stack)):
        temp+=stack.pop()

    return temp


# =========================
# 스택용도로 리스트를 활용한 케이스
# =========================
def break_brace(ted3: list) -> str:
    stack = []
    for i in range(len(ted3)):
        if len(stack) == 0:
            stack.append(ted3[i:i+1])
        else:
            if stack[-1] == '(':
                if ted3[i:i+1] == ')':
                    stack.pop()
                else:
                    stack.append(ted3[i:i+1])
            else:
                stack.append(ted3[i:i+1])

    return stack

def ted_sort(ted: list) -> list:

    heap = []
    result = []

    for i in ted:
        heapq.heappush(heap,-i)

    for i in range(len(heap)):
        result.append(-heapq.heappop(heap))

    return result


def count_element_by_range(a, left_value, right_value) -> int:
    left_index = bisect.bisect_left(a, left_value)
    right_index = bisect.bisect_right(a, right_value)

    return right_index - left_index


def uniq_count(a) -> dict:
    counter = Counter(a)

    return counter

def uniq_count2(a) -> dict:
    counter = Counter(a)

    return counter


def bfs(graph, start) -> list:
    visited = set()    # 방문했던곳인지 확인
    node = []          # graph의 특정점을 찾아가기위한
    route = []         # 순회기록
    node.append(start) # 초기화

    while node:
        ted = heapq.heappop(node)
        if ted not in visited: 
            for i in graph[ted]:
                if i not in visited:
                    heapq.heappush(node,i)

            route.append(ted)
            visited.add(ted)

    return route




# 재귀호출이 필요
def dfs(graph, start, route, visited=None) -> list:
    if not route:
        route.append(start)
    visited.add(start)   # 방문여부 확인


    for node in graph[start]:
        if node not in visited:
            route.append(node)
            visited.add(node)
        dfs(graph, node,route, visited)

    return route


    


# main example
if __name__ == "__main__":

    ted3 = "hello"

    # 1
    print(f"reversed_string={reversed_string_heapq(ted3)}")
    print(f"reversed_string={reversed_string_list(ted3)}")

    # 2
    ted3 = "((()))))"
    print(f"remainings={break_brace(ted3)}")

    # 3 heapq sorting (default:MinHeap, reverse: MaxHeap --)
    ted3 = [1,9,0,7,8,6,3,5]
    print(f"sorted={ted_sort(ted3)}")


    # 4. Count element
    a = [1, 2, 3, 3, 3, 5, 5, 7]
    print(f"how many={count_element_by_range(a, 2, 5)}")

    # 5. Uniq Count element
    a = ['a', 'b', 'c', 'c', 'c', 'd', 'd', 'f']
    print(f"how many={uniq_count(a)}") 

    # BFS (queue - heapq(list, value))
    print(bfs(graph, 'A'))

    # DFS
    route = []
    visited = set()
    print(dfs(graph, 'A',route, visited))
