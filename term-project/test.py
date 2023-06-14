import pytest
import random
import networkx as nx
from heuristic import KernighanLinAlgorithm

random.seed(0)

def test_swap_nodes_1():
    U, W = {1, 2, 3}, {4, 5, 6},
    a, b = 1, 4
    expected_U, expected_W = {2, 3, 4}, {1, 5, 6}

    algo = KernighanLinAlgorithm(None, None)
    U, W = algo.swap_nodes(U, W, a, b)

    assert U == expected_U
    assert W == expected_W


def test_swap_nodes_2():
    U, W = {1, 2}, {4, 5, 6},
    a, b = 2, 5
    expected_U, expected_W = {1, 2}, {4, 5, 6}

    algo = KernighanLinAlgorithm(None, None)
    U, W = algo.swap_nodes(U, W, a, b)

    assert U == expected_U
    assert W == expected_W


def test_compute_D_values_1():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
    U, W = {1, 2}, {3, 4}
    expected_D = {1: 1, 2: 0, 3: 1, 4: 0}

    algo = KernighanLinAlgorithm(G, None)
    function_D = algo.compute_D_values(U, W)

    assert function_D == expected_D

def test_compute_D_values_2():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 3), (3, 4)])
    U, W = {1, 4}, {2, 3}
    expected_D = {1: 2, 4: 2, 2: 1, 3: 1}

    algo = KernighanLinAlgorithm(G, None)
    function_D = algo.compute_D_values(U, W)
    
    assert function_D == expected_D


def test_initial_partition_1():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
    expected_U, expected_W = {1, 3}, {2, 4}

    algo = KernighanLinAlgorithm(G, None)
    U, W = algo.initial_partition()

    assert U == expected_U
    assert W == expected_W

def test_initial_partition_2():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 6),
                      (3, 6), (3, 5), (4, 5), (4, 6),
                      ])  
    expected_U, expected_W = {1, 2, 4}, {3, 5, 6}

    algo = KernighanLinAlgorithm(G, None)
    U, W = algo.initial_partition()

    assert U == expected_U
    assert W == expected_W

def test_compute_max_gain_1():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), 
                      (3, 4), (3, 5), (4, 5), (4, 6),
                      ])

    U, W = {1, 2, 3}, {4, 5, 6}
    D = {1: 1, 2: 0, 3: 2, 4: 0, 5: -1, 6: -1}
    expected_a, expected_b, expected_gain = 3, 6, 1

    algo = KernighanLinAlgorithm(G, None)
    a, b, gain = algo.compute_max_gain(U, W, D)

    assert a == expected_a
    assert b == expected_b
    assert gain == expected_gain

def test_compute_max_gain_2():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 6),
                      (3, 6), (3, 5), (4, 5), (4, 6),
                      ])  
    
    U, W = {1, 3, 4}, {2, 5, 6}
    D = {1: 1, 3: 1, 4: 2, 2: 0, 5: 3, 6: 1}
    expected_a, expected_b, expected_gain = 4, 5, 3

    algo = KernighanLinAlgorithm(G, None)
    a, b, gain = algo.compute_max_gain(U, W, D)

    assert a == expected_a
    assert b == expected_b
    assert gain == expected_gain

def test_calculate_cut_1():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3),
                      (3, 4), (3, 5), (4, 5), (4, 6),
                      ])
    
    U, W = {1, 2, 3}, {4, 5, 6}
    expected_cut = 3

    algo = KernighanLinAlgorithm(G, None)
    cut = algo.calculate_cut(U, W)

    assert cut == expected_cut


def test_calculate_cut_2():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 6),
                      (3, 6), (3, 5), (4, 5), (4, 6),
                      ])  
    
    U, W = {1, 3, 4}, {2, 5, 6}
    expected_cut = 6

    algo = KernighanLinAlgorithm(G, None)
    cut = algo.calculate_cut(U, W)

    assert cut == expected_cut

def test_case_1():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3),
                      (3, 4), (3, 5), (4, 5), (4, 6),
                      ])
    k = 3

    algo = KernighanLinAlgorithm(G, k)
    result = algo.run()

    assert result == True

def test_case_2():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 5), (2, 6),
                        (3, 6), (3, 5), (4, 5), (4, 6),
                        ])
    
    k = 2

    algo = KernighanLinAlgorithm(G, k)
    result = algo.run()

    assert result == False

def test_case_3():
    G = nx.Graph()
    
    for i in range(1, 7):
        G.add_node(i)
    
    k = 0

    algo = KernighanLinAlgorithm(G, k)
    result = algo.run()

    assert result == True

def test_case_4():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3),
                      (3, 4), (3, 5), (4, 5), (4, 6),
                      ])
    k = 8

    algo = KernighanLinAlgorithm(G, k)
    result = algo.run()

    assert result == True

def test_case_5():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3),
                      (3, 4), (3, 5), (4, 5), (4, 6),
                      ])
    k = 1

    algo = KernighanLinAlgorithm(G, k)
    result = algo.run()

    assert result == False

test_swap_nodes_1()
test_swap_nodes_2()
test_compute_D_values_1()
test_compute_D_values_2()
test_initial_partition_1()
test_initial_partition_2()
test_compute_max_gain_1()
test_compute_max_gain_2()
test_calculate_cut_1()
test_calculate_cut_2()

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()

print("All tests passed.")