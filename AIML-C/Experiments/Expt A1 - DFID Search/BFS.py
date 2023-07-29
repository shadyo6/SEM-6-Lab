# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 12:22:02 2022

@author: admin
"""

graph = {
  'A' : ['B','C'],
  'B' : ['D'],
  'C' : ['E','F'],
  'D' : ['G','H'],
  'E' : ['I','J'],
  'F' : ['K','L'],
  'G' : [],
  'H' : [],
  'I' : [],
  'J' : [],
  'K' : [],
  'L' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')    # function calling