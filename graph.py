import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def load_citation_network(file_path):
    graph = nx.DiGraph()  # Use DiGraph for a directed graph

    # Read the dataset and add nodes and edges to the graph
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("#"):  # Skip comment lines
                continue
            source, target = map(int, line.strip().split())
            graph.add_node(source)
            graph.add_node(target)
            graph.add_edge(source, target)

    return graph

def main():
    # Specify the file path of the dataset
    # dataset_path = "./Datasets/cit-HepPh.txt/Cit-HepPh.txt"
    dataset_path = "./Datasets/cit-HepPh.txt/sample.txt"

    try:
        # Load the citation network
        citation_network = load_citation_network(dataset_path)

        # Print basic graph statistics
        print("Nodes:", citation_network.number_of_nodes())
        print("Edges:", citation_network.number_of_edges())

        # Get node degrees for color mapping
        degrees = dict(citation_network.degree())
        node_colors = [degrees[node] for node in citation_network.nodes]

        # Plot the directed graph with gradient node colors based on degree
        seed = 13648
        pos = nx.spring_layout(citation_network, seed)

        # Use scatter to plot nodes with gradient colors
        plt.figure(figsize=(10, 8))
        nx.draw_networkx_nodes(citation_network, pos, node_size=50, node_color=node_colors, cmap=plt.cm.Blues, edgecolors='k', linewidths=0.5)
        nx.draw_networkx_edges(citation_network, pos, alpha=0.1)

        # Remove axis ticks
        plt.xticks([])
        plt.yticks([])

        # Add colorbar
        sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
        sm._A = []  # Fix for ScalarMappable
        cbar = plt.colorbar(sm, orientation='vertical', fraction=0.02, pad=0.1)
        cbar.set_label('Node Degree')

        plt.show()

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
