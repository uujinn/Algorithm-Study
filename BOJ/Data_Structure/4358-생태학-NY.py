from sys import stdin
tree_cnt = {}
tree_name = []
total = 0
while True:
    tree = str(stdin.readline().rstrip())
    if not tree: break #문자열이 비었으면 끝
    else:
        if tree in tree_cnt: tree_cnt[tree] += 1
        else: 
            tree_cnt[tree] = 1
            tree_name.append(tree)
        total += 1

for tree in sorted(tree_name):
    print("%s %.4f" %(tree, tree_cnt[tree]/total*100))