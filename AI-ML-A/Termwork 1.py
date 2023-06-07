from collections import defaultdict

tree = defaultdict(list)

def addEdge(u,v):
    tree[u].append(v)

def dfs(start,goal,depth):
    print(start,end=" ")
    if(start == goal):
        return True
    if(depth <= 0):
        return False
    for i in tree[start]:
        if dfs(i,goal,depth-1):
            return True
    return False

def dfid(start, goal, maxDepth):
    print('Start node: ', start, "Goal node: ", goal)
    for i in range(maxDepth):
        print("\nDFS at level: ", i+1)
        print("Path taken: ", end=" ")
        isPathFound = dfs(start,goal,i)
        if(isPathFound):
            print("\nGoal node found")
            return
    if(isPathFound == False):
        print("\nGoal not found!")



addEdge('1','2')
addEdge('1','3')
addEdge('1','4')
addEdge('2','5')
addEdge('2','6')
addEdge('4','7')
addEdge('4','8')
addEdge('5','9')
addEdge('5','10')
addEdge('7','11')
addEdge('7','12')
dfid('1','12',4)