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
    dataset_path = "./Datasets/cit-HepPh.txt/sample_5000.txt"

    try:
        # Load the citation network
        citation_network = load_citation_network(dataset_path)

        # Filter nodes based on degree
        degree_threshold = 10
        filtered_nodes = [node for node in citation_network.nodes if citation_network.degree(node) >= degree_threshold]
        filtered_network = citation_network.subgraph(filtered_nodes)

        # Get node degrees for color mapping
        filtered_degrees = dict(filtered_network.degree())
        node_colors = [filtered_degrees[node] for node in filtered_network.nodes]

        # Plot the directed graph with gradient node colors based on degree
        seed = 13648
        pos = nx.spring_layout(filtered_network, seed)

        # Use scatter to plot nodes with gradient colors
        plt.figure(figsize=(10, 8))

        # Use a colormap with all colors of VIBGYOR
        cmap = plt.cm.get_cmap("rainbow", len(node_colors))
        nx.draw_networkx_nodes(filtered_network, pos, node_size=50, node_color=node_colors, cmap=cmap, edgecolors='k', linewidths=0.5)
        nx.draw_networkx_edges(filtered_network, pos, alpha=0.1)

        # Remove axis ticks
        plt.xticks([])
        plt.yticks([])

        # Add colorbar based on the degree threshold
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=degree_threshold, vmax=max(node_colors)))
        sm._A = []  # Fix for ScalarMappable
        cbar = plt.colorbar(sm, orientation='vertical', fraction=0.02, pad=0.1)
        cbar.set_label(f'Node Degree >= {degree_threshold}')

        plt.show()

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()
