# Direct-Method-Beam-Stress-Calculator

The direct method calculator will take in information such as the number of elements, nodes, node locations, material characteristics, forces, and boundary conditions to calculate the final displacements. 

The 3 dof solver takes in global X, global Y, and Theta Z values and will compute those directional displacements. The method to input forces is also special. When asked to enter node forces enter those values with respect to the global coordinate system. For forces along a given element, you should calulate the loads at the joints due to such loads and compute the reaction forces. The program will ask for the reaction forces and will compute the correct force vector as a result. 

All computational results are saved to a .txt file. 
