from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

# 후위 순회 : left -> right -> root
def postOrder(nodes):
    if len(nodes) <= 1:
        return nodes
    
    for i in range(1, len(nodes)):        
        if nodes[0] < nodes[i]:
            return postOrder(nodes[1 : i]) + postOrder(nodes[i :]) + [nodes[0]]     # left + right + root
    return postOrder(nodes[1 :]) + [nodes[0]]


nodes = []
while True:
    try:
        nodes.append(int(stdin.readline()))
    except:
        break
    
nodes = postOrder(nodes)
for node in nodes:
    print(node)