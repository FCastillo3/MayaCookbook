import maya.cmds as cmds

def buttonFunction(args):
    cmds.polyCube()
    
def showUI():
    myWin = cmds.window(title="Button Example", widthHeight=(200, 200))
    cmds.columnLayout()
    cmds.button(label="Make Cube", command=buttonFunction)
    cmds.showWindow(myWin)
showUI()