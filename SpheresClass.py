import maya.cmds as cmds

class SpheresClass:

    def __init__(self):
        self.win = cmds.window(title="Make Spheres", widthHeight=(300, 200))
        cmds.columnLayout()
        self.numSpheres = cmds.intField(minValue=1)
        cmds.button(label="Make Spheres", command=self.makeSpheres)
        cmds.showWindow(self.win)
        
    def makeSpheres(self, *args):
        number = cmds.intField(self.numSpheres, query = True, value = True)
        for i in range(0, number):
            cmds.polySphere()
            cmds.move(i*2.2, 0, 0)
            
            
SpheresClass()