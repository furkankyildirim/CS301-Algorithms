import random
import networkx as nx
from typing import Any, Dict, List, Set, Tuple

class KernighanLinAlgorithm:
    def __init__(self, G: nx.Graph, k: int):
        self.Graph = G
        self.k = k

    def run(self):
        U, W = self.initial_partition()
        while True:
            D = self.compute_D_values(U, W)
            a, b, gain = self.compute_max_gain(U, W, D)
            
            if gain <= 0:
                distinct_edges = self.calculate_cut(U, W)

                if distinct_edges <= self.k:
                    print("Found a partition with at most k distinct edges.")
                    print("U = ", U)
                    print("W = ", W)
                    print("Distinct edges = ", distinct_edges)
                    return True

                
                else:
                    print("No partition with at most k distinct edges found.")
                    return False

            U, W = self.swap_nodes(U, W, a, b)

    def initial_partition(self) -> Tuple[Set[Any], Set[Any]]:
        nodes = list(self.Graph.nodes)
        random.shuffle(nodes)  # Ensure randomness of initial partition
        mid = len(nodes) // 2
        return set(nodes[:mid]), set(nodes[mid:])

    def compute_D_values(self, U: Set[Any], W: Set[Any]) -> Dict[Any, int]:
        D = {}
        for node in U:
            D[node] = sum(1 if neighbor in W else -1 for neighbor in self.Graph[node])

        for node in W:
            D[node] = sum(1 if neighbor in U else -1 for neighbor in self.Graph[node])

        return D

    def compute_max_gain(self, U: Set[Any], W: Set[Any], D: Dict[Any, int]) -> Tuple[Any, Any, int]:
        max_gain = float('-inf')
        for a in U:
            for b in W:
                cost = D[a] + D[b] - 2 * (1 if b in self.Graph[a] else 0)
                if cost > max_gain:
                    max_gain = cost
                    max_pair = a, b

        return max_pair[0], max_pair[1], max_gain

    def swap_nodes(self, U: Set[Any], W: Set[Any], a: Any, b: Any) -> Tuple[Set[Any], Set[Any]]:
        # Ensure the swap doesn't imbalance the sets
        if len(U) == len(W):
            U.remove(a)
            W.remove(b)
            U.add(b)
            W.add(a)

        return U, W

    def calculate_cut(self, U: Set[Any], W: Set[Any]) -> int:
        cut = sum(1 for a in U for b in W if a in self.Graph[b])
        return cut