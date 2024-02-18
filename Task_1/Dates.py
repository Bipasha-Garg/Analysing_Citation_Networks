import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def load_citation_network(file_path, date_file_path):
    graph = nx.DiGraph()

    # Load date information from the file
    date_dict = {}
    with open(date_file_path, 'r') as date_file:
        for line in date_file:
            if line.startswith("#"):
                continue
            paper_id, date_str = line.strip().split()
            date_dict[int(paper_id)] = date_str

    # Load citation network from the main file
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("#"):
                continue
            source, target = map(int, line.strip().split())
            graph.add_node(source, date=date_dict.get(source, ""))
            graph.add_node(target, date=date_dict.get(target, ""))
            graph.add_edge(source, target)

    return graph

def plot(filtered_degrees, filtered_network, degree_threshold):
    node_colors = [filtered_degrees[node] for node in filtered_network.nodes]
    seed = 13648
    pos = nx.spring_layout(filtered_network, seed)
    plt.figure(figsize=(10, 8))
    cmap = plt.cm.get_cmap("rainbow", len(node_colors))
    nx.draw_networkx_nodes(filtered_network, pos, node_size=50, node_color=node_colors, cmap=cmap, edgecolors='k', linewidths=0.5)
    nx.draw_networkx_edges(filtered_network, pos, alpha=0.1)
    
    date_labels = {node: filtered_network.nodes[node]['date'] for node in filtered_network.nodes}
    nx.draw_networkx_labels(filtered_network, pos, labels=date_labels, font_size=8, font_color='black')

    plt.xticks([])
    plt.yticks([])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=degree_threshold, vmax=max(node_colors)))
    sm._A = []  # Fix for ScalarMappable
    cbar = plt.colorbar(sm, orientation='vertical', fraction=0.02, pad=0.1)
    cbar.set_label(f'Node Degree >= {degree_threshold}')
    plt.show()

def main():
    dataset_path = "../Datasets/cit-HepPh.txt/sample_5000.txt"
    date_file_path = "../Datasets/cit-HepPh-dates.txt"

    try:
        citation_network = load_citation_network(dataset_path, date_file_path)
        degree_threshold = 0
        filtered_nodes = [node for node in citation_network.nodes if citation_network.degree(node) >= degree_threshold]
        filtered_network = citation_network.subgraph(filtered_nodes)
        filtered_degrees = dict(filtered_network.degree())
        plot(filtered_degrees, filtered_network, degree_threshold)

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()


