# DFS is recursive in nature, which goes depth by depth. In python, it uses the recursive call stack

"""
    Thinking Steps for DFS recursive approach
    1. In graphs, we can traverse one node again so we need a "visited" list to track the nodes visited.
    2. Use a set() to prevent duplicates, and also the check of node in visited is time efficient
    3. We start by checking if the visited is None, which is usually initialized in the parameters 
    4. If it is, then we initialise it to the set()
    5. If it is not, then we add the node as the data structure already exists and we can add in items
    6. Any processing of the node happens here
    7. Once we have visited a node, we have to check the child and keep going. 
    8. As we are going deep, we will use the for loop
    9. If the child is not in visited, then I am going to call recursion again and keep going deeper

    Assuming that we are given the graph, node, and visited is passed in the input. 

    Time Complexity: O(V+E) where V is the Vertices and E is Edges, which comes from traversing all V & E
    Space Complexity: O(V), which comes from the visited set and recursion call stack iverhead in the worst case

    Notes:
    1. Initializing the visited in the parameter itself prevents the Python's infamous mutable default agument bug

"""
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)

    # Processing of the node happens here if needed

    for neighbors in graph[node]:
        if neighbors not in visited:
            dfs_recursive(graph, neighbors, visited)