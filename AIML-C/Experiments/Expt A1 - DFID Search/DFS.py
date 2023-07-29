# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 13:00:34 2022

@author: admin
"""
def recursive_dfs(graph, source,path = []):
    if source not in path:
       path.append(source)
       if source not in graph:
          # leaf node, backtrack
            return path
       for neighbour in graph[source]:
           path = recursive_dfs(graph, neighbour, path)
    return path

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

path = recursive_dfs(graph, "A")
print(" ".join(path))