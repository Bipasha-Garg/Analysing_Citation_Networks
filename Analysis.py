import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import datetime 

def load_citation_network(file_path):
    graph = nx.DiGraph()  

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("#"):
                continue
            source, target = map(int, line.strip().split())
            graph.add_node(source)
            graph.add_node(target)
            graph.add_edge(source, target)

    return graph

def plot(filtered_degrees,filtered_network,degree_threshold):
    # degree_threshold =10
    node_colors = [filtered_degrees[node] for node in filtered_network.nodes]
    seed = 13648
    pos = nx.spring_layout(filtered_network, seed)
    plt.figure(figsize=(10, 8))
    cmap = plt.cm.get_cmap("rainbow", len(node_colors))
    nx.draw_networkx_nodes(filtered_network, pos, node_size=50, node_color=node_colors, cmap=cmap, edgecolors='k', linewidths=0.5)
    nx.draw_networkx_edges(filtered_network, pos, alpha=0.1)
    plt.xticks([])
    plt.yticks([])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=degree_threshold, vmax=max(node_colors)))
    sm._A = []  # Fix for ScalarMappable
    cbar = plt.colorbar(sm, orientation='vertical', fraction=0.02, pad=0.1)
    cbar.set_label(f'Node Degree >= {degree_threshold}')
    plt.show()


def analyze_connected_citations(citation_network, start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year + 1, 1, 1)  
    filtered_nodes = [node for node in citation_network.nodes if citation_network.nodes[node]['date'] and start_date <= datetime.strptime(citation_network.nodes[node]['date'], "%Y-%m-%d") < end_date]
    filtered_network = citation_network.subgraph(filtered_nodes)
    year_labels = {node: datetime.strptime(citation_network.nodes[node]['date'], "%Y-%m-%d").strftime("%Y") for node in filtered_network.nodes}
    unique_years = list(set(year_labels.values()))
    color_map = plt.cm.get_cmap('tab10', len(unique_years))
    node_colors = [color_map(unique_years.index(year)) for year in year_labels.values()]
    pos = nx.spring_layout(filtered_network, seed=42)
    print(f"Time Frame: {start_year}-{end_year}, Number of Nodes: {filtered_network.number_of_nodes()}, Number of Edges: {filtered_network.number_of_edges()}")
    return citation_network

def main():
    # dataset_path = "./Datasets/cit-HepPh.txt/Cit-HepPh.txt"
    # dataset_path = "./Datasets/cit-HepPh.txt/sample_100.txt"
    dataset_path = "./Datasets/cit-HepPh.txt/sample_5000.txt"

    try:
        citation_network = load_citation_network(dataset_path)
        degree_threshold = 5
        filtered_nodes = [node for node in citation_network.nodes if citation_network.degree(node) >= degree_threshold]
        filtered_network = citation_network.subgraph(filtered_nodes)
        filtered_degrees = dict(filtered_network.degree())
        filtered_network = analyze_connected_citations(filtered_network,2000,2001)
        # plot(filtered_degrees, filtered_network,degree_threshold)
        
        degree_dis(filtered_network)
        # diameter(filtered_network)
        clustering(filtered_network)
        # connectedness(filtered_network)
        community(filtered_network)
        vizualisation(filtered_network)

    except Exception as e:
        print("Error:", str(e))


def degree_dis(citation_network):
        degrees = [citation_network.degree(node) for node in citation_network.nodes]
        plt.hist(degrees, bins=20, alpha=0.7)
        plt.title('Degree Distribution')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')
        plt.show()

def diameter(citation_network):
    diameter = nx.diameter(citation_network)
    print(f'Graph Diameter: {diameter}')

def centrality(citation_network):
    degree_centrality = nx.degree_centrality(citation_network)
    betweenness_centrality = nx.betweenness_centrality(citation_network)
    closeness_centrality = nx.closeness_centrality(citation_network)

def clustering(citation_network):
    clustering_coefficient = nx.average_clustering(citation_network)
    print(f'Average Clustering Coefficient: {clustering_coefficient}')

def connectedness(citation_network):
    connected_components = nx.connected_components(citation_network)
    print(f'Number of Connected Components: {nx.number_connected_components(citation_network)}')

def community(citation_network):
    communities = nx.community.greedy_modularity_communities(citation_network)
    print(f'Number of Communities: {len(communities)}')

def vizualisation(citation_network):
    seed = 13648
    pos = nx.spring_layout(citation_network, seed)
    nx.draw(citation_network, pos, with_labels=True, node_size=50, alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
