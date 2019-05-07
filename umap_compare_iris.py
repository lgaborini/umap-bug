# Python standalone script

import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import umap

# Prepare data
iris = load_iris()

def draw_umap(data, labels, n_neighbors=15, min_dist=0.1, title='', close=True):
   fit = umap.UMAP(
      n_neighbors=n_neighbors,
      min_dist=min_dist,
      n_components=2
   )
   
   u = fit.fit_transform(data);
   
   if (close):
      plt.close('all')
   plt.scatter(u[:,0], u[:,1], c=labels, s=1)
   plt.title('nn = {}, d = {}'.format(n_neighbors, min_dist))
   plt.show()

### Sweep on `min_dist`
draw_umap(iris.data, iris.target, min_dist=0.001)
draw_umap(iris.data, iris.target, min_dist=0.1)
draw_umap(iris.data, iris.target, min_dist=0.99)

### Sweep on `n_neighbors`
draw_umap(iris.data, iris.target, n_neighbors=3)
draw_umap(iris.data, iris.target, n_neighbors=5)
draw_umap(iris.data, iris.target, n_neighbors=30)
