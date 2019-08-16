# fractal-tree

This code is to create a fractal tree over a surface discretized by triangles. It was developed to create a representation of the Purkinje network in the ventricles of the human heart.

Read the documentation in [fractal-tree.readthedocs.org](http://fractal-tree.readthedocs.org/en/latest/). 

The details of the algorithm are presented in this [article](http://www.sciencedirect.com/science/article/pii/S0021929015007332). If you are going to use this code, please cite:

	Generating Purkinje networks in the human heart.
	F. Sahli Costabal, D. Hurtado and E. Kuhl.
	Journal of Biomechanics, doi:10.1016/j.jbiomech.2015.12.025


**Pre-requisites:**

* Numpy
* Scipy

You will need .obj mesh file to create the tree. A very nice software to manipulate the mesh and export it to .obj is [MeshLab](http://meshlab.sourceforge.net). Please check if the mesh has duplicated vertex or faces before running the code. Also the orientation of the normals can change your results, because the angles will be flipped. To visualize the output, the best alternative is [Paraview](http://www.paraview.org).

To define the mesh file and the parameters of the tree to use, edit the parameters.py file and then run:

```
from FractalTree import *
from parameters import Parameters

param=Parameters()

branches, nodes = Fractal_Tree_3D(param)
```

If you have questions you can contact me at francisco.sahli  at  gmail.com

## Examples section:
##### Author: Lucas Berg

### How to run:

##### Step 1) Set up the parameters file:

The first thing that you need to do is configure the ***parameters.py***. 

|  Parameter | Description  |
| ------------ | ------------ |
|  meshfile |  path and filename to *.obj* file name |
|  filename |  name of the output files  |
| init_node  |  the first node of the tree  |
|  second_node  |  this point is only used to calculate the initial direction of the tree and is not included in the tree |
| init_length  | length of the first branch  |
| N_it  |  number of generations of branches |
| length  | average lenght of the branches in the tree  |
| std_length  | standard deviation of the length. Set to zero to avoid random lengths  |
| min_length  | minimum length of the branches.  |
| branch_angle  | angle with respect to the direction of the previous branch and the new branch  |
| w  | repulsivity parameter  |
| l_segment  | length of the segments that compose one branch  |
| Fascicles  | include one or more straigth branches with different lengths and angles from the initial branch |
| fascicles_angles  | angles with respect to the initial branches of the fascicles  |
| fascicles_length  | length  of the fascicles |
| save  | save text files containing the nodes, the connectivity and end nodes of the tree |
| save_paraview  | save a .vtu Paraview file |

###### TIP: How to parse meshes to *.obj* format

If you already have a mesh in *.vtu* or *.vtk* format you can parse it to *.obj* using Paraview together with Meshlab. 
Firstly, open the mesh on Paraview and apply the Extract Surface filter, then save it as *.stl*. The next step is to use another program called Meshlab and open the *.stl* on it. After that you can export the mesh in *.obj* format.

##### Step 2) Run the Python script:

Now just run the *create_fractal_tree.py* script.

```sh
$ python create_fractal_tree.py
```

### Samples:

##### Example 1) Purkinje network over a sphere:

```sh
$ cp Parameter-Config/parameters-sphere-sample.py parameters.py
$ python create_fractal_tree.py
```

##### Example 2) Purkinje network over a block:

```sh
$ cp Parameter-Config/parameters_block.py parameters.py
$ python create_fractal_tree.py
```

##### Example 3) Purkinje network over a Rabbit heart:

```sh
$ cp Parameter-Config/parameters_bunny.py parameters.py
$ python create_fractal_tree.py
```













