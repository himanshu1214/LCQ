adj_list = {
    "A": ["B", "D"], 
    "B":["A", "C"], 
    "C":["B"], 
    "D":["A", "E", "F"], 
    "E": ["D", "G", "F"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["G", "F"]
    }
from queue import Queue
from collections import defaultdict
def bfs_graph(adj_list):
    visited = defaultdict(str)
    level = defaultdict(str)
    parent = defaultdict(str)
    bfs_traversal_output = []
    que = Queue()

    first_node = "A"
    level[first_node] = -1
    que.put(first_node)

    while not que.empty():
        pop_node = que.get()
        if not visited[pop_node]:
            visited[pop_node] = True
            # print(visited) 
    
            bfs_traversal_output.append(pop_node)
            for node in adj_list[pop_node]:

                if visited[node]:
                    continue
                else:
                    visited[node] = False
                    parent[node] = pop_node
                    level[node] = level[pop_node] + 1

                    que.put(node)
                print(f"Node visiting : parent: {pop_node} and parent_status : {visited[pop_node]} and child : {node} and status : {visited[node]}")
    return bfs_traversal_output

print(bfs_graph(adj_list))
