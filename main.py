# # OUCC finals 2023 Lamps 2
# from collections import deque
#
#
# def changeCol(nums, k):
#     for j in range(5):
#         nums[j][k] = 1 - nums[j][k]
#
#
# def changeRow(nums, k):
#     for j in range(5):
#         nums[k][j] = 1 - nums[k][j]
#
#
# def makeHash(nums):
#     return str(nums)
#
#
# mat = []
# for _ in range(5):
#     mat.append([int(i) for i in input()])
# target = [[0] * 5 for _ in range(5)]
# visited = set()
# visited.add(makeHash(mat))
# q = deque()
# q.append(mat)
# numMoves = 0
#
# while q:
#     for _ in range(len(q)):
#         curr = q.popleft()
#
#         if curr == target:
#             print(numMoves)
#
#         for i in range(5):
#             newCurr = [[num for num in row] for row in curr]
#             changeCol(newCurr, i)
#             newCurrHash = makeHash(newCurr)
#             if newCurrHash not in visited:
#                 visited.add(newCurrHash)
#                 q.append(newCurr)
#
#             newCurr = [[num for num in row] for row in curr]
#             changeRow(newCurr, i)
#             newCurrHash = makeHash(newCurr)
#             if newCurrHash not in visited:
#                 visited.add(newCurrHash)
#                 q.append(newCurr)
#
#     numMoves += 1

# # OUCC finals 2020 Fastest Route
# import heapq
#
# edges = (
#     ('a', 'b', 1), ('a', 'c', 1), ('b', 'e', 3), ('c', 'd', 1), ('d', 'e', 1), ('d', 'f', 2), ('e', 'g', 1),
#     ('f', 'g', 1)
# )
# graph = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
# for x, y, weight in edges:
#     graph[x].append((y, weight))
#
# start, end = input().split()
#
# h = []
# heapq.heappush(h, (0, f"{start}"))
# visited = set()
#
# while h:
#     pathSum, path = heapq.heappop(h)
#     curr = path[-1]
#     if curr == end:
#         print(path)
#        break
#     visited.add(curr)
#     for neighbour, weight in graph[curr]:
#         if neighbour not in visited:
#             heapq.heappush(h, (pathSum + weight, path + neighbour))
# directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
#
#
# def score(arr, k, r, store, visited):
#     if (k, r) in visited:
#         return 0
#     visited.add((k, r))
#     if (k, r) in store:
#         return store[(k, r)]
#     if arr[k][r] == 9:
#         store[(k, r)] = 1
#         return 1
#     ret = 0
#     for (x, y) in directions:
#         if 0 <= k + x < len(arr) and 0 <= r + y < len(arr[0]):
#             if (k+x, r+y) in visited:
#                 continue
#             if arr[k+x][r+y] == arr[k][r] + 1:
#                 ret += score(arr, k + x, r + y, store, visited)
#     store[(k, r)] = ret
#     return ret
# def blink(arr):
#     temp = []
#     for num in arr:
#         # print(num)
#         n = len(num)
#         if num == '0':
#             temp.append('1')
#         elif n & 1:
#             temp.append(str(int(num) * 2024))
#         else:
#             n >>= 1
#             temp.append(str(int(num[:n])))
#             temp.append(str(int(num[n:])))
#     return temp
def dfs(coords, arr):
    currVal = arr[coords[0]][coords[1]]
    island = set()
    stack = [coords]
    while stack:
        curr = stack.pop()
        island.add(curr)
        visited.add(curr)
        x, y = curr
        for i, j in directions:
            newCurr = (x+i, y+j)
            if 0 <= x+i < len(arr) and 0 <= y + j < len(arr[0]) and newCurr not in island and arr[x+i][y+j] == currVal:
                stack.append(newCurr)
    return island


def area(group):
    return len(group)


def perimeter(group):
    ans = set()
    for x, y in group:
        for i, j in directions:
            if (x+i, y+j) not in group:
                ans.add((x+i, y+j))
    return ans


def count_islands(group):
    ans = 0
    for val in group.values():
        # print(val)
        val.sort()
        ans += 1
        for i in range(len(val)-1):
            if val[i] + 1 != val[i+1]:
                ans += 1
    return ans


def number_of_sides(group):
    sides = [{} for _ in range(4)]
    for x, y in group:
        idx = 0
        for i, j in directions:
            if (x+i, y+j) not in group:
                if idx < 2:
                    sides[idx][y+j] = sides[idx].get(y+j, []) + [x+i]
                else:
                    sides[idx][x+i] = sides[idx].get(x+i, []) + [y+j]
            idx += 1
    return sum(count_islands(subGroup) for subGroup in sides)


directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
field = []

with open("fences.txt") as fences:
    for line in fences.readlines():
        line = line.strip('\n')
        field.append(line)

partitions = []
visited = set()

for k in range(len(field)):
    for r in range(len(field[0])):
        if (k, r) not in visited:
            partitions.append(dfs((k, r), field))

ret = 0
for field_group in partitions:
    print(field_group)
    print(area(field_group), number_of_sides(field_group))
    ret += area(field_group) * number_of_sides(field_group)
print()
print(ret)
