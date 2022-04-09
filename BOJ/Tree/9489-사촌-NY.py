from sys import stdin
cousins = []

def dfs_k(nodes, k):
    while  

def find_cousins():
    

while True:
    n, k = map(int, stdin.readline().split())
    if n == k == 0: break
    nodes = {}
    nums = list(map(int, stdin.readline().split()))
    temp = []
    for idx, num in enumerate(nums):
        if num not in nodes:
            nodes[num] = []
        if nums[idx-1]+1 != num: #연속 끊겼음
            for key, val in sorted(nodes.items()):
                if len(val) == 0: 
                    nodes[key].extend(temp)
                    break
            temp = []
        else:
            temp.append(num)
    