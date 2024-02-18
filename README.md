# Analysing_Citation_Networks
This involves exploring the High-energy physics citation network. Arxiv HEP-PH (high energy physics phenomenology) citation graph is from the e-print arXiv. If a paper i cites paper j, the graph contains directed edge from i to j. If a paper cites, or is cited by, a paper outside the dataset, the graph does not contain any information about this. 


## References

    FOR PLOTTING:
    http://snap.stanford.edu/data/cit-HepPh.html  (citation network of physicists at hep-ph classification)
    https://networkx.org/documentation/stable/auto_examples/drawing/plot_directed.html 

    FOR ANALYSIS: 
    https://www.cs.rice.edu/~nakhleh/COMP571/Slides-Spring2015/GraphTheoreticProperties.pdf 
    https://www.analyticsvidhya.com/blog/2018/04/introduction-to-graph-theory-network-analysis-python-codes/


## Timeline


`Library Exploration`
    Explored the possibility of using the SNAP library for graph analysis but encountered version issues, leading to the decision to use NetworkX for building the graph.

`Graph Construction`
    Successfully constructed the citation network using NetworkX. Noted that the edge count is less than mentioned in the dataset documentation due to the representation of unordered pairs.

`Node Visualization`
    Implemented node visualization with different colors based on their degrees to visually inspect the density of the graph at nodes. This step provides an initial understanding of the distribution of citations.

`Matplotlib Performance Testing`
    Encountered performance challenges while plotting the entire graph using Matplotlib due to its large size. Conducted tests with a smaller dataset (from Datasets/cit-HepPh.txt/sample_5000.txt) successfully within a few seconds.

`Graph Plotting`
    Successfully plotted a subset of the graph containing 5000 points to provide a visual representation of the citation network. This step helps in gaining insights into the overall structure and connections within the high-energy physics community.

`Metric Analysis`

    Initiated the analysis of various metrics to understand the characteristics of the citation network. Metrics include degree distribution, centrality measures, clustering coefficient, connected components, graph diameter, community detection, and visualization techniques.

`Documentation and References`

    Referenced external sources such as Graph Theoretic Properties and Analytics Vidhya for guidance on graph analysis techniques.

`Larger dataset`
    Used a larger dataset of 12000 and 25500 points to get better analysis. The smaller dataset was used for testing purposes, but the larger one is needed for more accurate results.




#### Metrics used for  Analysis

``` Degree Distribution```

``` Centrality Measure ```

``` Clustering Coefficient```

``` Connected Components ```

``` Graph Diameter ```

``` Community Detection ```

``` Vizualisation ```



