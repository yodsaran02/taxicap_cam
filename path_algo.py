# importing the heapq to use the priority queue concept
import heapq
from numpy import Inf
def Dijkstra(graph, start):
    l = len(graph)
    
    # initialize all node distances as infinite
    dist = [Inf for _ in range(l)]
    
    # set the distance of starting node as 0
    dist[start] = 0
    
    # create a list that indicates if a node is visited or not
    vis = [False for _ in range(l)]
    
    # creating a priority queue
    pqueue = [(0, start)]
    
    # this while will run till there is some node to process 
    while len(queue) > 0:
        
        # we don't need the current node distance so use '_' as a variable for it.
        _, u = heapq.heappop(pqueue)
        
        # skip the node if it is visited
        if vis[u]:
            continue
            
        # set the current node as visited i.e True
        vis[u] = True
        
        for v, d in graph[u]:
            # now if the distance of the current node + the distance to the node we're visiting is less than the prior distance of the node we're visiting then update that distance and add that node to the priority queue
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                heapq.heappush(pqueue, (dist[v], v))
    
    # now at last return the list which contains the shortest path to each node from that given node
    return dist