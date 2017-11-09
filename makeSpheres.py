import maya.cmds as cmds

global sphereCountField
global sphereRadiusField

def showUI():
    global sphereCountField
    global sphereRadiusField
    
    myWin = cmds.window(title="Make Sphere", widthHeight= (300,200))
    cmds.columnLayout()
    sphereCountField = cmds.intField(minValue=1)
    sphereRadiusField = cmds.floatField(minValue=0.5)
    cmds.button(label="Make Spheres", command=makeSpheres)
    cmds.showWindow(myWin)
    
def makeSpheres(*args):
    global sphereCountField
    global sphereRadiusField
    
    numSpheres = cmds.intField(sphereCountField, query=True, value=True)
    myRadius = cmds.floatField(sphereRadiusField, query=True, value=True)
    
    for i in range(numSpheres):
        cmds.polySphere(radius=myRadius)
        cmds.move((i * myRadius * 2.2), 0, 0)
    
showUI()