graph = {
  'S' : ['A','B','C'],
  'A' : ['D','E'],
  'B' : ['F','G'],
  'C' : ['H'],
  'H' : ['I','J'],
  'I' : ['K','L','M'],
  'F' : ['K','L'],
  'D' : [],
  'E' : [],
  'F' : [],
  'G' : [],
  'K' : [],
  'L' : [],
  'M' : []
}

path = []
def IDDFS(root, goal):
    depth = 0
    while True:
        result = DLS(root, goal, depth)
        if result == goal:
            return result
        depth = depth + 1

def DLS(node, goal, depth):
    if node not in path:
       path.append(node)
    if depth == 0 and node == goal:
        print(" --- Found goal, returning --- ")
        return node
    elif depth > 0:
        for child in graph.get(node, []):
            if goal == DLS(child, goal, depth-1):
                return goal
IDDFS('S', 'I')
print(path)
