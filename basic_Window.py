import maya.cmds as cmds




def showUI():
    myWin = cmds.window(title="Simple Window", widthHeight=(300, 200))
    cmds.columnLayout()
    cmds.text(label="Hello, Maya!")
    cmds.showWindow(myWin)

    
showUI()