# Scalable Feature Learning for Networks

## SUMMARY

### Introduction
  The paper proposes node2vec, a framework for learning feature representations for nodes in networks12.
  The main idea is to use a flexible biased random walk procedure to sample diverse neighborhoods of nodes and optimize a network-aware objective function using stochastic gradient descent3.
  The paper claims that node2vec can capture both homophily and structural equivalence, two important notions of node similarity in networks, by tuning two parameters p and q that control the exploration strategy of the random walk.

### Methodology

  The paper defines a 2nd order random walk with transition probabilities that depend on the previous node in the walk, as well as the edge weights.
  The paper introduces the return parameter p and the in-out parameter q that bias the walk towards breadth-first or depth-first sampling, respectively.
  The paper uses the Skip-gram model to learn node embeddings that maximize the log-probability of preserving network neighborhoods, and approximates the partition function using negative sampling.
  The paper also shows how to extend node embeddings to edge embeddings using simple binary operators4.

### Experiments and Results

  The paper evaluates node2vec on two prediction tasks: multi-label classification and link prediction, on several real-world networks from diverse domains56.
  The paper compares node2vec with state-of-the-art feature learning methods, such as spectral clustering, DeepWalk, and LINE, as well as heuristic scores for link prediction.
  The paper demonstrates that node2vec outperforms the baselines by up to 26.7% on multi-label classification and up to 12.6% on link prediction, and is robust to perturbations and scalable to large networks7.
  The paper also analyzes the parameter sensitivity and the effect of different exploration strategies on the learned representations.

## The three major strengths of the paper

  The paper introduces a novel and flexible way of sampling network neighborhoods that can adapt to different network structures and prediction tasks, and generalizes prior work as special cases.
  The paper leverages the power of the Skip-gram model and negative sampling to efficiently learn low-dimensional and task-independent feature representations for nodes in networks.
  The paper provides extensive empirical evidence and analysis to support the effectiveness and efficiency of node2vec on various real-world networks and prediction tasks.

## The three major weaknesses of the paper

  The paper does not provide a clear theoretical justification or intuition for the choice of the parameters p and q, and how they relate to the notions of homophily and structural equivalence.
  The paper does not compare node2vec with other recent approaches for feature learning in networks, such as graph convolutional networks, graph attention networks, or graph neural networks, which could offer more expressive and powerful representations.
  The paper does not address the potential limitations or drawbacks of node2vec, such as the sensitivity to the random walk length, the scalability to very large and dynamic networks, or the interpretability of the learned embeddings.

## Three improvements

  The paper could provide a more rigorous theoretical analysis or a more intuitive explanation of the role and impact of the parameters p and q, and how they affect the properties and quality of the sampled neighborhoods and the learned embeddings.
  The paper could conduct a more comprehensive and fair comparison with other state-of-the-art feature learning methods, especially those based on graph neural networks, and highlight the advantages and disadvantages of node2vec over them.
  The paper could discuss the possible challenges or limitations of node2vec, such as the optimal choice of the random walk length, the scalability and efficiency issues for very large and dynamic networks, or the interpretability and visualization of the learned embeddings.
