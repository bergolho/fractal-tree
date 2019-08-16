# -*- coding: utf-8 -*-
"""
This module contains the Parameters class that is used to specify the input parameters of the tree.
"""

import numpy as np

class Parameters():
    """Class to specify the parameters of the fractal tree.
            
    Attributes:
        meshfile (str): path and filename to obj file name.
        filename (str): name of the output files.
        init_node (numpy array): the first node of the tree.
        second_node (numpy array): this point is only used to calculate the initial direction of the tree and is not included in the tree. Please avoid selecting nodes that are connected to the init_node by a single edge in the mesh, because it causes numerical issues.
        init_length (float): length of the first branch.
        N_it (int): number of generations of branches.
        length (float): average lenght of the branches in the tree.
        std_length (float): standard deviation of the length. Set to zero to avoid random lengths.
        min_length (float): minimum length of the branches. To avoid randomly generated negative lengths.
        branch_angle (float): angle with respect to the direction of the previous branch and the new branch.
        w (float): repulsivity parameter.
        l_segment (float): length of the segments that compose one branch (approximately, because the lenght of the branch is random). It can be interpreted as the element length in a finite element mesh.
        Fascicles (bool): include one or more straigth branches with different lengths and angles from the initial branch. It is motivated by the fascicles of the left ventricle. 
        fascicles_angles (list): angles with respect to the initial branches of the fascicles. Include one per fascicle to include.
        fascicles_length (list): length  of the fascicles. Include one per fascicle to include. The size must match the size of fascicles_angles.
        save (bool): save text files containing the nodes, the connectivity and end nodes of the tree.
        save_paraview (bool): save a .vtu paraview file. The tvtk module must be installed.
        
    """
    def __init__(self):
        self.meshfile='Mesh/ventricles.obj'				#self.meshfile='block_first_try.obj'
	
	# left ventricle
	self.filename='LV_Purkinje'				#self.filename='block_purkinje'
        self.init_node=np.array([53.3247, 74.5455, -13.0866])	#self.init_node=np.array([-1.0, 0.0, 0.0])
	self.second_node=np.array([58.1195, 71.2602, -30.4854])	#self.second_node=np.array(-0.964, 0.0, 0.266)
	
	# right ventricle
	#self.filename='RV_Purkinje'
	#self.init_node=np.array([44.6761, 67.9155, -5.0558])
	#self.second_node=np.array([48.7621, 62.6291, -15.961])	

	self.init_length=7 					#self.init_length = 0.5   			# 7 looks OK, maybe even shorter
#Number of iterations (generations of branches)
        self.N_it=15 						#self.N_it = 10					# 
#Median length of the branches
        self.length=5		 				#self.length =.3				# 3 works, should be longer
#Standard deviation of the length
        self.std_length = np.sqrt(0.2)*self.length								# I did not play with this parameter at all
#Min length to avoid negative length
        self.min_length = self.length/3										# interesting parameter
        self.branch_angle=0.07	 				#self.branch_angle=0.15				# probably should not be above 0.2
        self.w=0.03						#self.w=0.1					# should not be increased above 0.1
#Length of the segments (approximately, because the lenght of the branch is random)
	self.l_segment=0.1 					#self.l_segment=0.01				# 0.1 is fine for our model
        self.Fascicles=False 					#self.Fascicles=True				# no fascicles right now (for simiplicity)
###########################################
# Fascicles data
###########################################
        self.fascicles_angles=[-1.5,.2] #rad
        self.fascicles_length=[.5,.5]
# Save data?
        self.save=True
        self.save_paraview=True
