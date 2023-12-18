import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

file_path = "graph.txt"

def input_matrix(filename):
  with open(file_path, "r") as f:
    matrix1 = []
    for line in f:
      row = [int(x) for x in line.strip().split()]
      matrix1.append(row)
  return matrix1

def is_adjacency_matrix(matrix1):
  n = len(matrix1)
  for i in range(n):
    if len(matrix1[i]) != n:
      return False
    for j in range(n):
      if matrix1[i][j] < 0 :
        return False
  return True

def is_directed(matrix1):
  n = len(matrix1)
  for i in range(n):
    for j in range(n):
      if matrix1[i][j] != matrix1[j][i]:
        return True
  return False

def multigraph(matrix1):
  n = len(matrix1)
  for i in range(n):
    for j in range(n):
      if matrix1[i][j] > 1 or matrix1[i][i] > 0:
        return True
  return False

def plot(matrix1):
  print("Nodes of graph: ", len(matrix1))
  edges = []
  n = len(matrix1)
  if multigraph(matrix1)==False:
    for i in range(n):
      for j in range(n):
        if matrix1[i][j] != 0:
          print("Edge from", i, "to", j)
  else:
    for i in range(n):
      for j in range(n):
          print("There are", matrix1[i][j], "edges from", i, "to", j)
          edges.append(matrix1[i][j])
    # print(edges)
  if is_directed(matrix1):
    print("This is a directed graph:")
  else:
    print("This is an undirected graph:")

def degree_vertices(matrix1):
  n = len(matrix1)
  if multigraph(matrix1)==False:
    for i in range(n):
      degree = 0
      for j in range(n):
        if matrix1[i][j] != 0:
          degree += matrix1[i][j]
      print("Degree of vertex", i, "is", degree)
  else:
    for i in range(n):
      degree = 0
      for j in range(n):
        degree += matrix1[i][j]
        degree += matrix1[j][i]
      print("Degree of vertex", i, "is", degree)

def dfs(matrix1):
  n = len(matrix1)
  visited = [False] * n
  stack = []
  stack.append(0)
  visited[0] = True
  print("Travelsal_DFS start from vertex 0: ", end="")  
  while len(stack) != 0:
    v = stack.pop()
    print(v, end=" ")
    for i in range(n):
      if matrix1[v][i] != 0 and visited[i] == False:
        stack.append(i)
        visited[i] = True
  print()

def bfs(matrix1):
  n = len(matrix1)
  visited = [False] * n
  queue = []
  queue.append(0)
  visited[0] = True
  print("Travelsal_BFS starting from vertex 0: ", end="")
  while len(queue) != 0:
    v = queue.pop(0)
    print(v, end=" ")
    for i in range(n):
      if matrix1[v][i] != 0 and visited[i] == False:
        queue.append(i)
        visited[i] = True
  print()

def shortest_path(matrix1):
  n = len(matrix1)
  try:
    i = int(input("Enter the starting vertex: "))
    j = int(input("Enter the ending vertex: "))
    if i == "" or j == "" or i >= n or j >= n:
      raise ValueError
  except ValueError:
    print("Invalid vertex")
    return
  try:
    if matrix1[i][j] == 0:
      raise ValueError
  except ValueError:
    print("No path from", i, "to", j)
    return
  visited = [False] * n
  queue = []
  queue.append(i)
  visited[i] = True
  print("Shortest path from", i, "to", j, "is", end=" ")
  while len(queue) != 0:
    v = queue.pop(0)
    print(v, end=" ")
    for i in range(n):
      if matrix1[v][i] != 0 and visited[i] == False:
        queue.append(i)
        visited[i] = True
  print()

def main(matrix1):
  is_directed(matrix1)
  plot(matrix1)
  degree_vertices(matrix1)
  dfs(matrix1) 
  bfs(matrix1)
  shortest_path(matrix1)
  # G = nx.from_numpy_array(np.array(matrix1), create_using=nx.MultiGraph())
  # pos = nx.spring_layout(G,seed=1)
  # nx.draw_networkx(G, pos, node_color = 'r', node_size = 200, alpha = 1,with_labels=True,edgelist=[])
  # ax = plt.gca()
  # for e in G.edges:
  #     ax.annotate("",
  #                 xy=pos[e[0]], xycoords='data',
  #                 xytext=pos[e[1]], textcoords='data',
  #                 arrowprops=dict(arrowstyle="->", color="0.5",
  #                                 shrinkA=5, shrinkB=5,
  #                                 patchA=None, patchB=None,
  #                                 connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
  #                                 ),
  #                                 ),
  #                 )
  # plt.axis('off')
  # plt.show()
  
if __name__ == "__main__":
  if not is_adjacency_matrix(input_matrix("graph.txt")):
    print("Not an adjacency matrix")
    exit()
  matrix1 = input_matrix("graph.txt")
  main(matrix1)