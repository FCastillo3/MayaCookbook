import maya.cmds as cmds

class CustomMenu:

    def __init__(self):
    
        self.win = cmds.window(title="Menu Example", menuBar=True, widthHeight=(300,200))
        
        fileMenu = cmds.menu(label="File")
        loadOption = cmds.menuItem(label="Load")
        saveOption = cmds.menuItem(label="Save")
        cmds.setParent("..")
        
        self.menu = cmds.menu(label="Objects")
        sphereCommandMI = cmds.menuItem(label="Make Sphere", command=self.myCommand)
        sphereCommandMIOption = cmds.menuItem(optionBox=True, label="Make Sphere", command=self.myCommandOptions)
        cubeOption = cmds.menuItem(label="Make Cube", command=self.makeCube)
        cmds.setParent("..")
        
        cmds.columnLayout()
        cmds.text(label="Put the rest of your interface here")
        
        cmds.showWindow(self.win)
        
    def myCommand(self, *args):
        self.makeSphere(1)
    
    def myCommandOptions(self, *args):
        promptInput = cmds.promptDialog(title="Sphere Radius", message='Specify Radius: ', button=['OK', 'CANCEL'], defaultButton='OK', cancelButton='CANCEL', dismissString='CANCEL')
        
        if (promptInput == 'OK'):
            radiusInput = cmds.promptDialog(query=True,text=True)
            self.makeSphere(radiusInput)
    
    def makeSphere(self, sphereRadius):
        cmds.polySphere(radius=sphereRadius)
        
    def makeCube(self, *args):
        cmds.polyCube()
        
CustomMenu()