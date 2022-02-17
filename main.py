from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

def dijkstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path
    
// Test case for given question no. 2 in question set
givenGraph = Graph()
givenGraph.addNode("0")
givenGraph.addNode("1")
givenGraph.addNode("2")
givenGraph.addNode("3")
givenGraph.addNode("4")
givenGraph.addNode("5")
givenGraph.addNode("6")
givenGraph.addNode("7")
givenGraph.addNode("8")
givenGraph.addEdge("0", "1", 4)
givenGraph.addEdge("0", "7", 8)
givenGraph.addEdge("1", "2", 8)
givenGraph.addEdge("1", "7", 11)
givenGraph.addEdge("2", "8", 2)
givenGraph.addEdge("2", "3", 7)
givenGraph.addEdge("2", "5", 4)
givenGraph.addEdge("7", "8", 7)
givenGraph.addEdge("7", "6", 1)
givenGraph.addEdge("8", "6", 6)
givenGraph.addEdge("6", "5", 2)
givenGraph.addEdge("3", "5", 14)
givenGraph.addEdge("3", "4", 9)
givenGraph.addEdge("5", "4", 10)

print(dijkstra(givenGraph, "0"))
