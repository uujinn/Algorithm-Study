from sys import stdin
cousins = []

def find_cousins(nodes, k):
    k_parent, k_depth = map(int, nodes[k])
    count = 0
    for key, val in nodes.items():
        if val[1] == k_depth and val[0] != k_parent:
            count += 1
    cousins.append(count)
    
while True:
    n, k = map(int, stdin.readline().split())
    if n == k == 0: break
    nums = list(map(int, stdin.readline().split()))
    nodes = {nums[0]:[None, 0]}
    temp = []
    prev_prnt_idx = 0
    for idx in range(1, n):
        if nums[idx] not in nodes:
            nodes[nums[idx]] = []
        if idx == n-1 or nums[idx+1]-1 != nums[idx]: #연속 끊겼음
            parent = sorted(nodes.items())[prev_prnt_idx]
            parent_depth = parent[1][1]
            temp.append(nums[idx])
            for t in temp:
                nodes[t].append(parent[0])
                nodes[t].append(parent_depth+1)
            prev_prnt_idx += 1
            temp = []
        else:
            temp.append(nums[idx])
    find_cousins(nodes, k)
            
for c in cousins:
    print(c)