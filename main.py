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
