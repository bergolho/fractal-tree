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
        
	self.meshfile='Mesh/Patient_Pat03.obj'
	# Right Ventricle Patient 3
	self.filename='RV_Purkinje'				
        self.init_node=np.array([48.1611,66.6877,-4.0])	
	self.second_node=np.array([31.8936,95.7124,-27.5481])	
	self.init_length=1					
	#Number of iterations (generations of branches)
        self.N_it=20						
	#Median length of the branches
        self.length=6.0		 				
	#Standard deviation of the length
        self.std_length = np.sqrt(0.2)*self.length							
	#Min length to avoid negative length
        self.min_length = self.length/2										
        self.branch_angle=0.3				
        self.w=0.03						
	#Length of the segments (approximately, because the lenght of the branch is random)
	self.l_segment=0.1 					
        self.Fascicles=False 					
	
	# Left Ventricle Patient 3
	#self.filename='LV_Purkinje'
	#self.init_node=np.array([54.2261,76.7894,-4.0])
	#self.second_node=np.array([65.8646,66.4769,-35.5479])	

	#self.init_length=5					
	#Number of iterations (generations of branches)
        #self.N_it=10						 
	#Median length of the branches
        #self.length=4		 				
	#Standard deviation of the length
        #self.std_length = np.sqrt(0.2)*self.length						
        #self.min_length = self.length/3										
        #self.branch_angle=0.08	 				
        #self.w=0.03						
	#Length of the segments (approximately, because the lenght of the branch is random)
	#self.l_segment=0.1 					
        #self.Fascicles=False 					
###########################################
# Fascicles data
###########################################
        self.fascicles_angles=[-1.5,.2] #rad
        self.fascicles_length=[.5,.5]
# Save data?
        self.save=True
        self.save_paraview=True
