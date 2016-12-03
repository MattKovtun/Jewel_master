
desc = """
    File which was used to make machine learning and create examples of gems
    """


import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


folders = ['b_', 'r_', 'y_', 'w_', 'g_', 'p_', 'o_']
X = []
y = []
for i in range(len(folders)):
    folder = folders[i]
    num = len(os.listdir(folder)) // 2
    for j in range(num):
        img = np.reshape(np.load(folder + '/' + str(j) + '.npy'), -1)
        X.append(img)
        y.append(i)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

val = np.reshape(np.load('tests/58.npy'), -1)

print(neigh.predict([val]))