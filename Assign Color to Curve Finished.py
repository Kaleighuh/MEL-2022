import maya.cmds as cmds

def AssignNURBScolor(color):
    selection = cmds.ls(sl=1)
    name = cmds.ls(s=1)
    y = 1

    for x in selection:
        cmds.setAttr(name[y]) + ".overrideEnabled", 1)
        cmds.setAttr(name[y] + ".overrideColor" , color)
        y += 1

AssignNURBScolor(15)
