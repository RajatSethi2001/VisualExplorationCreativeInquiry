import igl
import scipy as sp
import numpy as np
import meshplot
from meshplot import plot, subplot, interact

meshplot.offline()
v, f = igl.read_triangle_mesh("contour3.ply")
k = igl.gaussian_curvature(v, f)
m = igl.massmatrix(v, f, igl.MASSMATRIX_TYPE_VORONOI)
minv = sp.sparse.diags(1 / m.diagonal())
kn = minv.dot(k)
l = igl.cotmatrix(v, f)
hn = -minv.dot(l.dot(v))
h = np.linalg.norm(hn, axis=1)

#plot(v, f, k)

#file = open("test.txt", "w")
#file.write(np.array2string(k))
#file.close()
np.savetxt("test2.txt", k)
print(k)