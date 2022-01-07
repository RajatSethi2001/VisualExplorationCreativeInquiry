import igl
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

v, f = igl.read_triangle_mesh("contour3.ply")
k = igl.gaussian_curvature(v, f)