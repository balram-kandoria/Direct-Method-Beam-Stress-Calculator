# Direct-Method-Beam-Stress-Calculator

The direct method calculator takes in information such as the number of elements, nodes, node locations, material characteristics, forces, and boundary conditions to calculate the final displacements. This program is intended to relieve some of the hand work of solving tedious beam deflection problems but also to serve as a check to already calculated values.

The 3 dof solver takes in global X, global Y, and Theta Z values and will compute those directional displacements. The method to input forces is also special. When asked to enter node forces enter those values with respect to the global coordinate system. For forces along a given element, you should calulate the loads at the joints due to such loads and compute the reaction forces. The program will ask for the reaction forces and will compute the correct force vector as a result.  

Input Directions: (Determine the type of units you will enter, unit conversions are NOT carried out by the program)

1.) "Problem Name: " - Enter a simple name to identify the problem. You don't need to enter .txt or any other file identifier, that is already taken care of in the code.

2.) "Number of Elements: " - Enter the number of elements. Make sure to label elements in your problem before hand so you can easily reference it in the resulting solution ticket. Not keep element numbers consitent will lead to invalid results and or confusion when interpreting the results.

3.) "Number of Nodes: " - Enter the number of nodes. Again follow the warning said in Input Direction 2.

4.) "X Location for Node #: " - Input the x location of the node requested. If entering 0, simply enter 0 and 00 will result in an error.

5.) "Y Location for Node #: " - Input the y location of the node requested. Make sure to keep units constant.

6.) "Element # Node start: " - Input the starting node number (NOT location) of the requested element. Elements are characterized by their starting and ending nodes. Elements will commonly share starting and ending nodes, its important to display this relationship when inputing this data. For example, Element 1 can start at Node 1 and end at Node 2 while Element 2 can start at Node 2 and end at Node 3.

7.) "Element # Node end: " Input ending node number (NOT location) of the requested element. Follow the same rules stated in problem 6.

8.) "Node # Boundary Type: " - Enter the number corresponding to the boundary type the node has. If a node simply connects two elements together it can be characterized as a free end.

9.) "Enter Node # X Force: " - Enter the force in the x direction inlcuding a component of a force vector. Note these are applied forces only which are forces specifically located at nodes. 

10.) "Enter Node # Y Force: " - Enter the force in the y direction inlcuding a component of a force vector. Again this is asking for the applied force

11.) "Enter Node # Theta_Z Moment: " - Enter the moment in the theta_z direction. This step is asking for the applied moment not a reactionary one.

12.) "Enter Node #'s X Reaction Force: " This is the x component of any reactions due to either a force/moment not location at a node or a distributed load across a element. 

All computational results are saved to a .txt file. 

Example Results:

Number of Elements: 3

Number of Nodes: 4

Node 1 Location [X,Y]: [0,0]

Node 2 Location [X,Y]: [3,0]

Node 3 Location [X,Y]: [5,0]

Node 4 Location [X,Y]: [7,0]


Element 1 Location [Node Start, Node End]: [1,2]

Element 2 Location [Node Start, Node End]: [2,3]

Element 3 Location [Node Start, Node End]: [3,4]


Node 1 Boundary Type: Free End [1,1,1]

Node 2 Boundary Type: Free End [1,1,1]

Node 3 Boundary Type: Free End [1,1,1]

Node 4 Boundary Type: Built In Support [0,0,0]


Boundary Displacements: [ 

                          x1

                          y1
                          
                          theta_z_1
                          
                          x2
                          
                          y2
                          
                          theta_z_2
                          
                          x3
                          
                          y3
                          
                          theta_z_3
                          
                          0
                          
                          0
                          
                          0 ]

Forces Located at Nodes : [ 

                            0.0
                            
                          -60000.0
                          
                          -150000.0
                          
                          0.0
                          
                          -60000.0
                          
                          150000.0
                          
                          0.0
                          
                          60000.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0 ]

Forces Located Along Elements : [ 
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0 ]

Forces = A - Ar : [ 

                          0.0
                          
                          -60000.0
                          
                          -150000.0
                          
                          0.0
                          
                          -60000.0
                          
                          150000.0
                          
                          0.0
                          
                          60000.0
                          
                          0.0
                          
                          0.0
                          
                          0.0
                          
                          0.0 ]

------------------------------------------------------------------------------------------------------------------------------

Element 1

Start Node: 1

End Node: 2

Length: 3.0

Area: 1.0

Elastic Modulus: 1.0

Moment of Inertia: 1.0

Angle: 0.0

Local Matrix

        0.33333              0              0       -0.33333              0              0
              0        0.44444        0.66667              0       -0.44444        0.66667
              0        0.66667        1.33333              0       -0.66667        0.66667
       -0.33333              0              0        0.33333              0              0
              0       -0.44444       -0.66667              0        0.44444       -0.66667
              0        0.66667        0.66667              0       -0.66667        1.33333


Global Matrix

        0.33333            0.0            0.0       -0.33333            0.0            0.0
            0.0        0.44444        0.66667            0.0       -0.44444        0.66667
            0.0        0.66667        1.33333            0.0       -0.66667        0.66667
       -0.33333            0.0            0.0        0.33333            0.0            0.0
            0.0       -0.44444       -0.66667            0.0        0.44444       -0.66667
            0.0        0.66667        0.66667            0.0       -0.66667        1.33333


------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------

Element 2

Start Node: 2

End Node: 3

Length: 2.0

Area: 1.0

Elastic Modulus: 1.0

Moment of Inertia: 1.0

Angle: 0.0

Local Matrix

            0.5              0              0           -0.5              0              0
              0            1.5            1.5              0           -1.5            1.5
              0            1.5            2.0              0           -1.5            1.0
           -0.5              0              0            0.5              0              0
              0           -1.5           -1.5              0            1.5           -1.5
              0            1.5            1.0              0           -1.5            2.0


Global Matrix

            0.5            0.0            0.0           -0.5            0.0            0.0
            0.0            1.5            1.5            0.0           -1.5            1.5
            0.0            1.5            2.0            0.0           -1.5            1.0
           -0.5            0.0            0.0            0.5            0.0            0.0
            0.0           -1.5           -1.5            0.0            1.5           -1.5
            0.0            1.5            1.0            0.0           -1.5            2.0


------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------

Element 3

Start Node: 3

End Node: 4

Length: 2.0

Area: 1.0

Elastic Modulus: 1.0

Moment of Inertia: 1.0

Angle: 0.0

Local Matrix

            0.5              0              0           -0.5              0              0
              0            1.5            1.5              0           -1.5            1.5
              0            1.5            2.0              0           -1.5            1.0
           -0.5              0              0            0.5              0              0
              0           -1.5           -1.5              0            1.5           -1.5
              0            1.5            1.0              0           -1.5            2.0


Global Matrix

            0.5            0.0            0.0           -0.5            0.0            0.0
            0.0            1.5            1.5            0.0           -1.5            1.5
            0.0            1.5            2.0            0.0           -1.5            1.0
           -0.5            0.0            0.0            0.5            0.0            0.0
            0.0           -1.5           -1.5            0.0            1.5           -1.5
            0.0            1.5            1.0            0.0           -1.5            2.0


------------------------------------------------------------------------------------------------------------------------------

Global System Matrix

        0.33333            0.0            0.0       -0.33333            0.0            0.0            0.0            0.0            0.0            0.0            0.0            0.0
            0.0        0.44444        0.66667            0.0       -0.44444       -0.66667            0.0            0.0            0.0            0.0            0.0            0.0
            0.0        0.66667        1.33333            0.0        0.66667        0.66667            0.0            0.0            0.0            0.0            0.0            0.0
       -0.33333            0.0            0.0        0.83333            0.0            0.0           -0.5            0.0            0.0            0.0            0.0            0.0
            0.0       -0.44444        0.66667            0.0        1.94444        0.83333            0.0           -1.5           -1.5            0.0            0.0            0.0
            0.0       -0.66667        0.66667            0.0        0.83333        3.33333            0.0            1.5            1.0            0.0            0.0            0.0
            0.0            0.0            0.0           -0.5            0.0            0.0            1.0            0.0            0.0           -0.5            0.0            0.0
            0.0            0.0            0.0            0.0           -1.5            1.5            0.0            3.0            0.0            0.0           -1.5           -1.5
            0.0            0.0            0.0            0.0           -1.5            1.0            0.0            0.0            4.0            0.0            1.5            1.0
            0.0            0.0            0.0            0.0            0.0            0.0           -0.5            0.0            0.0            0.5            0.0            0.0
            0.0            0.0            0.0            0.0            0.0            0.0            0.0           -1.5            1.5            0.0            1.5           -1.5
            0.0            0.0            0.0            0.0            0.0            0.0            0.0           -1.5            1.0            0.0           -1.5            2.0


Reduced Global System Matrix

        0.33333            0.0            0.0       -0.33333            0.0            0.0            0.0            0.0            0.0
            0.0        0.44444        0.66667            0.0       -0.44444       -0.66667            0.0            0.0            0.0
            0.0        0.66667        1.33333            0.0        0.66667        0.66667            0.0            0.0            0.0
       -0.33333            0.0            0.0        0.83333            0.0            0.0           -0.5            0.0            0.0
            0.0       -0.44444        0.66667            0.0        1.94444        0.83333            0.0           -1.5           -1.5
            0.0       -0.66667        0.66667            0.0        0.83333        3.33333            0.0            1.5            1.0
            0.0            0.0            0.0           -0.5            0.0            0.0            1.0            0.0            0.0
            0.0            0.0            0.0            0.0           -1.5            1.5            0.0            3.0            0.0
            0.0            0.0            0.0            0.0           -1.5            1.0            0.0            0.0            4.0


Reduced Force Vector : [ 

                            0.0
                            
                          -60000.0
                          
                          -150000.0
                          
                          0.0
                          
                          -60000.0
                          
                          150000.0
                          
                          0.0
                          
                          60000.0
                          
                          0.0 ]

Displacement Solution : [ 

                            0.0
                            
                          -280222.7903579254
                          
                          39401.022644265846
                          
                          -0.0
                          
                          101504.74799123437
                          
                          -125084.00292184067
                          
                          0.0
                          
                          133294.37545653753
                          
                          69335.28122717307
                          
                          0
                          
                          0
                          
                          0 ]

