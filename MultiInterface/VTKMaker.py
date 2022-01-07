import pyvista
import meshio
import igl
import scipy as sp
import numpy as np
import meshplot
from meshplot import plot, subplot, interact

file_name = "contour2"
file_ext = "ply"
file_total = f"{file_name}.{file_ext}"

meshplot.offline()
v, f = igl.read_triangle_mesh(file_total)
k = igl.gaussian_curvature(v, f)

mesh = meshio.read(file_total)
field_data = mesh.point_data
field_data['curvature'] = k
mesh.write(f"new_{file_name}.vtk")

#mesh = pyvista.PolyData(file_total)
#mesh.add_field_data(k, 'curvature')
#mesh.save(f"new_{file_name}.vtk")