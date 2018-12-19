# hierarchical agglomerative clustering
# fourgrams

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

import pandas as pd

# Assign spreadsheet filename to `file`
# sheet "results" contains raw data, "Sheet1" normalized, "Sheet2" rescaled
file = 'results1.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Load the sheet with rescaled data
X = xl.parse('Sheet2',header=-1)
X1 = X.iloc[:,0:24]

# generate the linkage matrix
Z = linkage(X1, method='ward',metric='euclidean')
#Z = linkage(X, method='average',metric='euclidean')
#Z = linkage(X, method='average',metric='cosine')

# calculate cophenetic distance
#from scipy.cluster.hierarchy import cophenet
#from scipy.spatial.distance import pdist

#c, coph_dists = cophenet(Z, pdist(X))
#print(c)

# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram (Fourgrams)')
plt.xlabel('text number')
plt.ylabel('distance')
dendrogram(
           Z,
           leaf_rotation=90.,  # rotates the x axis labels
           leaf_font_size=8.,  # font size for the x axis labels
           )
plt.savefig('dendrogram_fourgram.eps', format='eps', dpi=1000)
plt.show()





