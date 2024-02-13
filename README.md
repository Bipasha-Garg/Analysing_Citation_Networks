# Analysing_Citation_Networks
This involves exploring the High-energy physics citation network. Arxiv HEP-PH (high energy physics phenomenology) citation graph is from the e-print arXiv. If a paper i cites paper j, the graph contains directed edge from i to j. If a paper cites, or is cited by, a paper outside the dataset, the graph does not contain any information about this. 


## References
    http://snap.stanford.edu/data/cit-HepPh.html  (citation network of physicists at hep-ph classification)
    https://networkx.org/documentation/stable/auto_examples/drawing/plot_directed.html 


## Timeline

    - Tried to use snap library but failed due to some version issues to build the graph.
    - used networkx and it worked
    - but the number of nodes obtained is: 34546 and Edges: 420921; the number of edges are less than that mentioned in the dataset doc since there  each unordered pair of nodes is saved once only. therefore it is accounted once only while making the graph.


### STEPS
        - made the graph network using networkx
        - then tried to draw the nodes with different colors based on their degrees to get the density of the graph at the nodes
        - plotting the graph using matplotlib took a lot of time since the dataset is huge. But for a smaller dataset ot was verified well within a second or two. (smaller dataset, a small subset from the original dataset ,stored in Datasets/cit-HepPh.txt/sample.txt)
        - graph plotted with 5000 points taken from the dataset
        

