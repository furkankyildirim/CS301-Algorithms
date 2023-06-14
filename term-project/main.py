from brute import BruteForceAlgorithm
from heuristic import KernighanLinAlgorithm
import networkx as nx
import random
import time
import pandas as pd

def sample_generator(n: int) -> nx.Graph:
    """
    Generates a random graph with n nodes and returns it.

    Args:
        n (int): The number of nodes in the graph.

    Returns:
        A random graph with n nodes.
    """

    # create an empty graph object
    G = nx.Graph()

    # add nodes to the graph
    for i in range(n):
        G.add_node(i)
    
    # add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            # randomly decide whether to add an edge between nodes i and j
            if random.random() < 0.5:
                G.add_edge(i, j)

    # return the graph
    return G   

def main():
    n_set = [24]
    data = []
    for n in n_set:
        for _ in range(200):
            G = sample_generator(n)
            edge_count = G.number_of_edges()

            k_dict = {'0': 0, 'k': edge_count,
                      'k/2': edge_count // 2,
                      'random': random.randint(0, edge_count)
                      }

            for k in k_dict:
                algo = BruteForceAlgorithm(G, k_dict[k])
                start_time = time.time()
                brute_result = algo.run()
                brute_time = time.time() - start_time


                algo = KernighanLinAlgorithm(G, k_dict[k])
                start_time = time.time()
                heuristic_result = algo.run()
                heuristic_time = time.time() - start_time

                data.append((n, edge_count, k_dict[k], k, brute_time, brute_result, heuristic_time, heuristic_result))

                # Add the results to the dataframe
                # df = df.append({'n': n, 'k': k_dict[k], 'k_type': k, 'heuristic': heuristic_time, 'brute': None}, ignore_index=True)

    df = pd.DataFrame(data, columns=['n', 'm', 'k', 'k_type', 'brute_time', 'brute_result', 'heuristic_time', 'heuristic_result'])
    df.to_csv('analysis_24.csv', index=False)

if __name__ == "__main__":
    main()