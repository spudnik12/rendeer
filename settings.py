from enum import Enum

ShadingMode = Enum('ShadingMode', 'unlit flatDiffuse wireframe') #shading modes (don't modify this)

yRotation = 70 #rotation of the mesh on the Y axis (in degrees)
xRotation = 90 #rotation of the mesh on the X axis (in degrees)
zRotation = 0 #rotation of the mesh on the Z axis (in degrees)

lightDirectionX = 0 #rotation of the light source (in degrees)
lightDirectionY = -50 #rotation of the light source (in degrees)
lightDirectionZ = -20 #rotation of the light source (in degrees)

shadingMode = ShadingMode.flatDiffuse

calculateVertexNormals = False

diffuseColor = [20, 10, 170] #diffuse color on the lightest face of the mesh
unlitColor = [10, 200, 40] #color that applies to the whole mesh in unlit shading mode
wireframeColor = [200, 200, 200]

lightVector = [[1, 0, 0]] #initial position of the source of light, relative to the center (0, 0, 0)
    
meshPosition = [1, 1, -0.3] #position of the mesh. duh

renderFaceNormals = False #should it render the normals of the faces?
renderHardVertexNormals = False #should it render the hard normals of the vertices?
renderSoftVertexNormals = False #should it render the soft normals of the vertices?
renderMeshCenter = False #should it render the center of the mesh?
renderFaceCenters = False #should it render the centers of the faces?
renderLightSource = False #should it render the source of light and its direction?

cameraPosition = [1, 1, -2] #position of the camera

imagePlaneZ = 0 #position of the plane (on the Z axis)