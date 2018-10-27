import numpy as np
#from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage.transform import resize
IMG_DIM = 50
def make_ax(grid=False):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.grid(grid)
    return ax

# filled = np.array([
    # [[1, 0, 1], [0, 0, 1], [0, 1, 0]],
    # [[0, 1, 1], [1, 0, 0], [1, 0, 1]],
    # [[1, 1, 0], [1, 1, 1], [0, 0, 0]]
# ])

# ax = make_ax(True)
# ax.voxels(filled, edgecolors='gray')
# plt.show()

# ax = make_ax()
# ax.voxels(filled, facecolors='#1f77b430', edgecolors='gray')
# plt.show()

# ax = make_ax()
# ax.voxels(np.ones((3, 3, 3)), facecolors='#1f77b430', edgecolors='gray')
# plt.show()

# filled = np.load("gyroidUniform.npy")
# resized = resize(filled, (IMG_DIM, IMG_DIM, IMG_DIM), mode='constant')
# ax = make_ax(True)
# ax.voxels(resized, edgecolors='gray')
# plt.show()

filled = np.load("Merged.npy")
resized = resize(filled, (IMG_DIM, IMG_DIM, IMG_DIM), mode='constant')
ax = make_ax(True)
ax.voxels(resized, edgecolors='gray')
plt.show()