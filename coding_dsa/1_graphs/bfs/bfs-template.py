# BFS is iterative in nature, it goes level by level 

"""
    Thinking Steps for BFS
    1. In graphs, we can traverse one node again so we need a "visited" list to track the nodes visited and put the startNode in it 
    2. I need a queue, as we will be traversing level by level, and I initialise the startNode in it
    3. While there are items in the queue, first I need to get the node, which is by popleft() method
    4. After popping, this is where I am going to do any of the processing or printing needed 
    5. We need to consider the node child, which is through a for loop so we go through them
    6. We are to add all the child in the visited array and queue which are not in the visited array. 

    Assuming that we are given the graph and startNode as the input 

    Time Complexity: O(V+E) where V is the Vertices and E is Edges, which comes from traversing all V & E
    Space Complexity: O(V), which comes from the queue and visited set
"""
from collections import deque

def bfs(graph, startNode):
    visited = set([startNode])
    queue = deque([startNode])

    while queue:
        node = queue.popleft()

        # Processing or printing of the node happens here
        
        for neighbors in graph[node]:
            if neighbors not in visited:
                visited.add(neighbors)
                queue.append(neighbors)