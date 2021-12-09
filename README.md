# Direct-Method-Beam-Stress-Calculator

The direct method calculator will take in information such as the number of elements, nodes, node locations, material characteristics, forces, and boundary conditions to calculate the final displacements. 

The 3 dof solver takes in global X, global Y, and Theta Z values and will compute those directional displacements. The method to input forces is also special. When asked to enter node forces enter those values with respect to the global coordinate system. For forces along a given element, you should calulate the loads at the joints due to such loads and compute the reaction forces. The program will ask for the reaction forces and will compute the correct force vector as a result. 

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

