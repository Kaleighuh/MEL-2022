import maya.cmds as cmds

def SequentialRenamer(newName):

    selection = cmds.ls(sl=1)

    numCount = newName.count("#")
    numAmount = ("#" * numCount)
    pNewName = newName.partition(numAmount)

    pre = pNewName[0]
    num = pNewName[1]
    suffix = pNewName[2]

    i = 1
    for x in selection:
        num = str(i).zfill(numCount)
        finalName = (pre + num + suffix)
        cmds.select(x)
        cmds.rename(finalName)
        i += 1

SequentialRenamer("leg_##_int")