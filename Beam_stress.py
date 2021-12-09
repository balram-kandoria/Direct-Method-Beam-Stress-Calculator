'''By:  Balram Kandoria'''
'''Contact: balramkandoria@gmail.com'''
import numpy as np


'''Boundary Conditions'''
builtInSupport = (0, 0, 0);
simpleSupport = (0, 0, 1);
rollerSupportX = (1, 0, 1);
rollerSupportY = (0, 1, 1);
freeEnd = (1, 1, 1);

# Assumptions:
#   Constant Cross Sectional Area
#   2-D Truss NOT 3D Beam
name = input("Problem Name: ")
f = open(name+".txt", "w")




'''Stiffness Matrix Method'''
def localStiffnessMatrix(A, E, L, Iz):
    localK = [
        [((A*E)/L), 0, 0, ((-1*A*E)/L), 0, 0],
        [0, ((12*E*Iz)/(L**3)), ((6*E*Iz)/(L**2)), 0, ((-12*E*Iz)/(L**3)), ((6*E*Iz)/(L**2))],
        [0, ((6*E*Iz)/(L**2)), ((4*E*Iz)/L), 0, ((-6*E*Iz)/(L**2)), ((2*E*Iz)/L)],

        [((-A*E)/L), 0, 0, ((A*E)/L), 0, 0],
        [0, ((-12*E*Iz)/(L**3)), ((-6*E*Iz)/(L**2)), 0, ((12*E*Iz)/(L**3)), ((-6*E*Iz)/(L**2))],
        [0, ((6*E*Iz)/(L**2)), ((2*E*Iz)/L), 0, ((-6*E*Iz)/(L**2)), ((4*E*Iz)/L)]

    ]
    return localK

def transformationMatrix(theta):
    angle = theta
    T = [
        [np.cos(angle), np.sin(angle), 0, 0, 0, 0],
        [-np.sin(angle), np.cos(angle), 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, np.cos(angle), np.sin(angle), 0],
        [0, 0, 0, -np.sin(angle), np.cos(angle), 0],
        [0, 0, 0, 0, 0, 1]
        ]
    return T

def prettyPrint(x):
    print(f"{'Table' : >8}")
    for i in range(len(x)):
        for j in range(len(x)):
            print(f"{round(x[i][j],5) : >15}",end='')
        print()
    print()

def prettyPrintVector(x):
    for i in range(len(x)):
        print(f"{round(x[i],5) : >15}",end='')
        print()
    print()


# Define Elements
numberOfElements = int(input('Number of Elements: '));
f.write("Number of Elements: " + str(numberOfElements))
f.write("\n")
f.write("\n")
# Define Nodes
numberOfNodes = int(input('Number of Nodes: '));
f.write("Number of Nodes: " + str(numberOfNodes))
f.write("\n")
f.write("\n")
# Node Locations
nodeLocations = {};
for i in range(numberOfNodes):
    x = input('X Location for Node '+str(i+1)+": ")
    y = input('Y Location for Node ' + str(i+1) + ": ")
    nodeLocations["Node" + str(i+1)] = [float(x), float(y)];
    f.write("Node " + str(i+1) +" Location [X,Y]: ["+ str(x)+","+str(y)+"]")
    f.write("\n")
f.write("\n")
# Relate Nodes to Elements
elementNodeLocations = {};
elementNodeRelationship = {};
for i in range(numberOfElements):
    s = input("Element "+str(i+1)+" Node Start: ")
    e = input("Element "+str(i+1)+" Node End: ")
    Start = str(s);
    End = str(e);
    elementNodeLocations["Element" + str(i+1)] = [nodeLocations["Node" + Start], nodeLocations["Node" + End]];
    elementNodeRelationship["Element" + str(i+1)] = [int(Start), int(End)];
    f.write("Element " + str(i+1) +" Location [Node Start, Node End]: ["+ str(Start)+","+str(End)+"]")
    f.write("\n")
f.write("\n")
print(elementNodeLocations);
print(elementNodeRelationship);
# Place Boundaries
boundaryDisplacements = []
#Comment: Constraints are ordered x, y, z, thetax, thetay, thetaz
for i in range(numberOfNodes):
    boundaryInfo = int(input("Node "+str(i+1)+" Boundary Type: builtInSupport (1), simpleSupport (2), rollerSupportX (3), rollerSupportY (4), freeEnd (5) "))
    # Set Boundary Info to Actual Boundary Contraints
    if boundaryInfo == 1:
        boundaryType = builtInSupport;
        f.write("Node " + str(i+1) +" Boundary Type: Built In Support [0,0,0]")
        f.write("\n")
    elif boundaryInfo == 2:
        boundaryType = simpleSupport;
        f.write("Node " + str(i+1) +" Boundary Type: Simple Support [0,0,1]")
        f.write("\n")
    elif boundaryInfo == 3:
        boundaryType = rollerSupportX;
        f.write("Node " + str(i+1) +" Boundary Type: Roller Support (X Direction Free) [1,0,1]")
        f.write("\n")
    elif boundaryInfo == 4:
        boundaryType = rollerSupportY;
        f.write("Node " + str(i+1) +" Boundary Type: Roller Support (Y Direction Free) [0,1,1]")
        f.write("\n")
    elif boundaryInfo == 5:
        boundaryType = freeEnd;
        f.write("Node " + str(i+1) +" Boundary Type: Free End [1,1,1]")
        f.write("\n")


    tempVector = [];
    if boundaryType[0] == 1:
        tempVector += [("x"+ str(i+1))];
    else:
        tempVector += [0];

    if boundaryType[1] == 1:
        tempVector += [("y"+ str(i+1))];
    else:
        tempVector += [0];

    if boundaryType[2] == 1:
        tempVector += [("theta_z_"+ str(i+1))];
    else:
        tempVector += [0];
    boundaryDisplacements += tempVector

print(boundaryDisplacements)
f.write("\n")
for i in range(len(boundaryDisplacements)):
    if i == 0:
        f.write("Boundary Displacements: [ " + str(boundaryDisplacements[i]))
        f.write("\n")
    elif i != 0 and i != (len(boundaryDisplacements)-1):
        f.write("                          " + str(boundaryDisplacements[i]))
        f.write("\n")
    else:
        f.write("                          " + str(boundaryDisplacements[i]) + " ]")
        f.write("\n")
f.write("\n")
# Place Forces
NodeForces = [];
for i in range(numberOfNodes):
    tempVector = []
    tempVector += [float(input("Enter Node " + str(i+1) + "'s X Force: "))]
    tempVector += [float(input("Enter Node " + str(i+1) + "'s Y Force: "))]
    tempVector += [float(input("Enter Node " + str(i+1) + "'s Z Moment Force: "))]
    NodeForces += tempVector

print(NodeForces)

f.write("Forces Located at Nodes")
for i in range(len(NodeForces)):
    if i == 0:
        f.write(" : [ " + str(NodeForces[i]))
        f.write("\n")
    elif i != 0 and i != (len(NodeForces)-1):
        f.write("                          " + str(NodeForces[i]))
        f.write("\n")
    else:
        f.write("                          " + str(NodeForces[i]) + " ]")
        f.write("\n")
f.write("\n")


# Input Reaction Forces
reactionForces = []
for i in range(numberOfNodes):
    tempVector = []
    tempVector += [float(input("Enter Node " + str(i+1) + "'s X Reaction Force: "))]
    tempVector += [float(input("Enter Node " + str(i+1) + "'s Y Reaction Force: "))]
    tempVector += [float(input("Enter Node " + str(i+1) + "'s Z Reaction Moment Force: "))]
    reactionForces += tempVector
print(reactionForces)

f.write("Forces Located Along Elements")
for i in range(len(reactionForces)):
    if i == 0:
        f.write(" : [ " + str(reactionForces[i]))
        f.write("\n")
    elif i != 0 and i != (len(reactionForces)-1):
        f.write("                          " + str(reactionForces[i]))
        f.write("\n")
    else:
        f.write("                          " + str(reactionForces[i]) + " ]")
        f.write("\n")
f.write("\n")

forces = []
for i in range(len(reactionForces)):
    forces += [NodeForces[i] - reactionForces[i]]
print("Forces")
print(forces)

f.write("Forces = A - Ar")
for i in range(len(forces)):
    if i == 0:
        f.write(" : [ " + str(forces[i]))
        f.write("\n")
    elif i != 0 and i != (len(forces)-1):
        f.write("                          " + str(forces[i]))
        f.write("\n")
    else:
        f.write("                          " + str(forces[i]) + " ]")
        f.write("\n")
f.write("\n")

# Define Nodes
# Get Constants
# Fill Matrix
K = np.zeros((numberOfNodes*3,numberOfNodes*3))

for i in range(numberOfElements):
    A = float(input('Element ' + str(i+1) + ' Area: '))
    E = float(input('Element ' + str(i+1) + ' Elastic Modulus: '))
    Iz = float(input('Element ' + str(i+1) + ' Moment of Inertia: '))
    L = ((elementNodeLocations['Element'+str(i+1)][1][1] - elementNodeLocations['Element'+str(i+1)][0][1])**2 + ( elementNodeLocations['Element'+str(i+1)][1][0] - elementNodeLocations['Element'+str(i+1)][0][0])**2)**(0.5)

    k = localStiffnessMatrix(A, E, L, Iz)
    if ((( elementNodeLocations['Element'+str(i+1)][1][0])) - (elementNodeLocations['Element'+str(i+1)][0][0])) == 0:
        theta = (np.pi/2)
    else:
        theta = np.arctan(((elementNodeLocations['Element'+str(i+1)][1][1]) - (elementNodeLocations['Element'+str(i+1)][0][1])) / ((( elementNodeLocations['Element'+str(i+1)][1][0])) - (elementNodeLocations['Element'+str(i+1)][0][0])))

    T = transformationMatrix(theta)
    k_transformed = np.matmul(np.matmul(T,k), np.transpose(T))
    Start = elementNodeRelationship["Element" + str(i+1)][0];
    End = elementNodeRelationship["Element" + str(i+1)][1];
    print("Element" + str(i))
    print("Length: "+str(L))
    print(theta)
    print("Start")
    print(Start)
    prettyPrint(k_transformed)
    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")
    f.write("Element " + str(i+1))
    f.write("\n")
    f.write("Start Node: "+str(Start))
    f.write("\n")
    f.write("End Node: "+str(End))
    f.write("\n")
    f.write("Length: "+str(L))
    f.write("\n")
    f.write("Area: "+str(A))
    f.write("\n")
    f.write("Elastic Modulus: "+str(E))
    f.write("\n")
    f.write("Moment of Inertia: "+str(Iz))
    f.write("\n")
    f.write("Angle: "+str(theta))
    f.write("\n")
    f.write("\n")

    f.write("Local Matrix")
    f.write("\n")
    for i in range(len(k)):
        for j in range(len(k)):
            f.write(f"{round(k[i][j],5) : >15}")
        f.write("\n")
    f.write("\n")
    f.write("\n")

    f.write("Global Matrix")
    f.write("\n")
    for i in range(len(k_transformed)):
        for j in range(len(k_transformed)):
            f.write(f"{round(k_transformed[i][j],5) : >15}")
        f.write("\n")
    f.write("\n")
    f.write("\n")

    f.write("------------------------------------------------------------------------------------------------------------------------------")
    f.write("\n")

    for j in range(3):
        for l in range(3):
            # Start, Start
            x = Start
            y = Start
            K[int(3*(x)-3) + j][int(3*(y)-3) + l] += k_transformed[j][l]

            # Start, End
            x = Start
            y = End
            K[int(3*(x)-3) + j][int(3*(y)-3) + l] += k_transformed[j+int(3)][l]

            # End, End
            x = End
            y = End
            K[int(3*(x)-3) + j][int(3*(y)-3) + l] += k_transformed[j+int(3)][l+int(3)]

            # End, Start
            x = End
            y = Start
            K[int(3*(x)-3) + j][int(3*(y)-3) + l] += k_transformed[j][l+int(3)]


prettyPrint(K)

f.write("Global System Matrix")
f.write("\n")
for i in range(len(K)):
    for j in range(len(K)):
        f.write(f"{round(K[i][j],5) : >15}")
    f.write("\n")
f.write("\n")
f.write("\n")

system = np.zeros((numberOfNodes*3,numberOfNodes*3))

for i in range(len(forces)):
    for j in range(len(forces)):
        system[i][j] = K[i][j]

keepVector = []
for i in range(len(forces)):
    flag = False
    for j in range(len(forces)):
        if boundaryDisplacements[i] == 0:
            flag = True
            system[i][j] = 0
            system[j][i] = 0
    if boundaryDisplacements[i] != 0:
        keepVector += [i]

prettyPrint(system)
print(keepVector)
mod = int(len(keepVector))
reducedMatrix = np.zeros((mod,mod))
reducedVector = []
for i in range(len(keepVector)):
    reducedVector += [forces[keepVector[i]]]
    for j in range(len(keepVector)):
        reducedMatrix[i][j] = system[keepVector[i]][keepVector[j]]

prettyPrint(reducedMatrix)

f.write("Reduced Global System Matrix")
f.write("\n")
for i in range(len(reducedMatrix)):
    for j in range(len(reducedMatrix)):
        f.write(f"{round(reducedMatrix[i][j],5) : >15}")
    f.write("\n")
f.write("\n")
f.write("\n")

print(reducedVector)

f.write("Reduced Force Vector")
for i in range(len(reducedVector)):
    if i == 0:
        f.write(" : [ " + str(reducedVector[i]))
        f.write("\n")
    elif i != 0 and i != (len(reducedVector)-1):
        f.write("                          " + str(reducedVector[i]))
        f.write("\n")
    else:
        f.write("                          " + str(reducedVector[i]) + " ]")
        f.write("\n")
f.write("\n")

x = np.linalg.solve(reducedMatrix,reducedVector)
count = 0
for i in range(len(boundaryDisplacements)):
    if boundaryDisplacements[i] != 0:
        boundaryDisplacements[i] = x[count]
        count += 1


print()
print("Solution")
print(x)
print()
print(boundaryDisplacements)

f.write("Displacement Solution")
for i in range(len(boundaryDisplacements)):
    if i == 0:
        f.write(" : [ " + str(boundaryDisplacements[i]))
        f.write("\n")
    elif i != 0 and i != (len(boundaryDisplacements)-1):
        f.write("                          " + str(boundaryDisplacements[i]))
        f.write("\n")
    else:
        f.write("                          " + str(boundaryDisplacements[i]) + " ]")
        f.write("\n")
f.write("\n")


