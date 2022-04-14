from sys import stdin
input = stdin.readline

def getPostList(preList, pStart, pEnd, inList, iStart, iEnd):

    if pEnd - pStart <= 1: return preList[pStart:pEnd]
    root = preList[pStart]
    iRoot = inList.index(root)
    pMid = (pStart+1)+(iRoot-iStart)
    postList = []
    postList += getPostList(preList, pStart+1, pMid, inList, iStart, iRoot)
    postList += getPostList(preList, pMid, pEnd, inList, iRoot+1, iEnd)
    postList += [root]
    return postList

T = int(input())
for i in range(T):

    N = int(stdin.readline())
    preList = list(map(int, input().split()))
    inList = list(map(int, input().split()))

    postList = getPostList(preList, 0, len(preList), inList, 0, len(inList))
    print(' '.join(map(str, postList)))