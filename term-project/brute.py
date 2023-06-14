import networkx as nx
import itertools

class BruteForceAlgorithm:

    def __init__(self, G: nx.Graph, k: int):
        self.Graph = G
        self.k = k

    def run(self):
        for comb in itertools.combinations(self.Graph.nodes, self.Graph.number_of_nodes()//2):
            U = set(comb)
            W = set(self.Graph.nodes) - U
            
            distinct_edges = 0
            for i, j in self.Graph.edges:
                if (i in U and j in W) or (i in W and j in U):
                    distinct_edges += 1
            
            if distinct_edges <= self.k:
                print("Found a partition with at most k distinct edges.")
                print("U = ", U)
                print("W = ", W)
                print("Distinct edges = ", distinct_edges)
                return True

        print("No partition with at most k distinct edges found.")
        return False
