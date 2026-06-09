# DFS can be written to make it iterative in nature. 
# This is essentially crucial if the graph is too deep, which can exhaust the recursion call stack and lead to issues such as StackOverFlowError or RecursionError. 
# The solution is to manually manage own stack to prevent the error from happening. 
"""
    Thinking Steps for DFS recursive approach
    1. In graphs, we can traverse one node again so we need a "visited" list to track the nodes visited.
    2. Use a set() to prevent duplicates, and also the check of node in visited is time efficient
    3. As we are using our own stack, I need to initialize it and put the starting node into it
    4. While there are items in the stack, I need to pop the node first
    5. Check if the node is not in visited, if it is not, then I need to add it 
    6. Processing of the node happens here if needed
    7. I extend the child of the node in reversed order in the stack so that we can still maintain the LIFO order and process in the correct order

    Assuming that we are given the graph and startNode is passed in the input. 

    Time Complexity: O(V+E) where V is the Vertices and E is Edges, which comes from traversing all V & E
    Space Complexity: O(V), which comes from the visited set and our created stack
"""
def dfs_iterative(graph, startNode):
    visited = set()
    stack = [startNode]

    while stack:
        node = stack.pop()
        if node not in visited:

            visited.add(node)
            # Processing of the node happens here if needed

            # Reverse neighbors to maintain standard DFS order on a LIFO stack 
            stack.extend(reversed(graph[node]))