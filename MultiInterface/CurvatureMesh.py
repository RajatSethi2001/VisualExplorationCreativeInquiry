import pymeshlab

mesh_set = pymeshlab.MeshSet()

file_name = input("Enter file name: ")
mesh_set.load_new_mesh(file_name)
mesh_set.discrete_curvatures()

extension_index = file_name.index(".")
file_name = file_name[0:extension_index]
mesh_set.save_current_mesh(f"new_{file_name}.json")
