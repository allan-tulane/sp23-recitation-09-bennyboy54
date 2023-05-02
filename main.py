from collections import deque
from heapq import heappush, heappop


def shortest_shortest_path(graph, source):

  def pathfinder(visited, frontier):
    if len(frontier) == 0:
      return visited
    else:
      distance, node, num_edges = heappop(frontier)
      if node in visited:
        return pathfinder(visited, frontier)
      else:
        visited[node] = (distance, num_edges)
        for neighbor, weight in graph[node]:
          heappush(frontier, (distance + weight, neighbor, num_edges + 1))
        return pathfinder(visited, frontier)

  frontier = []
  heappush(frontier, (0, source, 0))
  visited = {}
  pathfinder(visited, frontier)
  return visited



def test_shortest_shortest_path():

  graph = {
    's': {('a', 1), ('c', 4)},
    'a': {('b', 2)},  # 'a': {'b'},
    'b': {('c', 1), ('d', 4)},
    'c': {('d', 3)},
    'd': {},
    'e': {('d', 0)}
  }
  result = shortest_shortest_path(graph, 's')

  assert result['s'] == (0, 0)
  assert result['a'] == (1, 1)
  assert result['b'] == (3, 2)
  assert result['c'] == (4, 1)
  assert result['d'] == (7, 2)


def bfs_path(graph, source):

    parents = {vertex: None for vertex in graph.keys()}
    parents[source] = source
  
    queue = deque([source])
  
    while len(queue) != 0:
        current = queue.popleft()
        for neighbor in graph[current]:
            if parents[neighbor] is None:
                parents[neighbor] = current
                queue.append(neighbor)

    return parents
   


def get_sample_graph():
  return {'s': {'a', 'b'}, 'a': {'b'}, 'b': {'c'}, 'c': {'a', 'd'}, 'd': {}}

def test_bfs_path():
  graph = get_sample_graph()
  parents = bfs_path(graph, 's')
  assert parents['a'] == 's'
  assert parents['b'] == 's'
  assert parents['c'] == 'b'
  assert parents['d'] == 'c'

 
def get_path(parents, destination):
    path = []
    current = destination
    while current != parents[current]:
        path.insert(-1, current)
        current = parents[current]
    path.reverse()
    path.remove(path[0])
    path.insert(0,list(parents.keys())[0])
    return ''.join(path)

  

graph = get_sample_graph()

parents = bfs_path(graph, 's')
print(parents)
print(get_path(parents, 'd'))
def test_get_path():
  graph = get_sample_graph()
  parents = bfs_path(graph, 's')
  assert get_path(parents, 'd') == 'sbc'
