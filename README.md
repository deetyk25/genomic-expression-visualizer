# genomic-expression-visualizer

This project explores gene expression data through visualization and basic preprocessing.
The goal is to better understand how computational choices (filtering, normalization)
affect biological signal interpretation.

## Stage 1 Progress
- Loaded and cleaned gene expression data: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE312485
- Filtered low-expression genes
- Applied log normalization
- Visualized expression distributions and gene-level variability

## Stage 2 Progress
- Implemented a PCA algorithm to highlight significant relationships explaining variance in the sampled genes.
- Implemented k-means clustering to represent the low-dimensional relationships in a plot


## How to Run
jupyter notebook notebooks/(*notebook name goes here*)

## Dependencies
pandas\
numpy\
matplotlib\
seaborn\
scikit-learn\
jupyter
