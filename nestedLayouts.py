import maya.cmds as cmds

class NestedLayouts:

    def __init__(self):
        self.win = cmds.window(title="Nested Layouts", widthHeight=(300,200))
        cmds.columnLayout()
        
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Input One:")
        self.inputOne = cmds.intField()
        cmds.setParent("..")
        
        cmds.rowLayout(numberOfColumns=2)
        cmds.text(label="Input Two:")
        self.inputTwo = cmds.intField()
        cmds.setParent("..")
        
        cmds.showWindow(self.win)

NestedLayouts()