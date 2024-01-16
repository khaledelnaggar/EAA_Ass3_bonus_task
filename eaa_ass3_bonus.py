import random
import networkx as nx

'''
Language: Python

To run the file run the command:

pip3 install -r requirements.txt && python3 eaa_ass3_bonus.py

or

pip install -r requirements.txt && python eaa_ass3_bonus.py

This program uses networkx and the command installs it beforehand if it fails installing it,
try installing networkx manually and then run the program >> python3 eaa_ass3_bonus.py

in the directory of the program
'''

# Parameters:
# Takes input graph and number of colors available delta +1
#
# Returns:
# A dictionary as  {node : color}
number_of_iteration = 0


def random_coloring(graph, num_colors):
    global number_of_iteration
    number_of_iteration = 0
    color_mapping = {node: None for node in graph.nodes()}

    # a getter for available colors for a vertex (excluding neighbour colors)
    def unique_colors(vertex):
        neighbor_colors = {color_mapping[neighbor] for neighbor in graph.neighbors(vertex)}
        set_of_unique_colors = set()
        for color in range(num_colors):
            if color not in neighbor_colors:
                set_of_unique_colors.add(color)
        return set_of_unique_colors

    # until all vertices get colored
    while None in color_mapping.values():
        number_of_iteration += 1
        # Each uncolored vertex tries to find a random candidate color
        coloring_suggested = {}
        for vertex, color in color_mapping.items():
            if color is None:
                suggested_colors = unique_colors(vertex)
                if suggested_colors:
                    suggested_colors = list(suggested_colors)
                    coloring_suggested[vertex] = suggested_colors[random.randint(0, len(suggested_colors) - 1)]
                else:
                    continue

        # Check if a neighbour has the same colour as the node
        for vertex, color_suggested in coloring_suggested.items():
            flag = True
            for neighbor in graph.neighbors(vertex):
                if coloring_suggested.get(neighbor) == color_suggested:
                    flag = False
                    # reject the suggested coloring and go for one more iteration
                    break
            if flag:
                color_mapping[vertex] = color_suggested
    return color_mapping


def test_case(graph):
    max_degree = max(dict(graph.degree()).values())
    print(f'Max Degree >> {max_degree}\n')
    coloring = random_coloring(graph, (max_degree + 1))
    print('Number of iterations elapsed: ', number_of_iteration)
    print(f'\n\nGraph >>> {graph.edges}')
    print(f'\n\nColors representation >> {coloring}')
    for u, v in graph.edges():
        if coloring[u] == coloring[v]:
            print('\nFailure: Not proper coloring')
            return False
    print('\nSuccess: proper coloring')
    print('Number of iterations elapsed: ', number_of_iteration)
    return True


graph_1 = nx.erdos_renyi_graph(200, 0.5)
graph_2 = nx.erdos_renyi_graph(400, 0.5)
graph_3 = nx.erdos_renyi_graph(700, 0.5)
graph_4 = nx.erdos_renyi_graph(820, 0.5)

test_case(graph=graph_1)
test_case(graph=graph_2)
test_case(graph=graph_3)
test_case(graph=graph_4)
