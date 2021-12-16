import maya.cmds as cmds
import sys 

def importMayaScript(nameFolder):

    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'import_script_maya_python/'+str(nameFolder)+'/'

    sys.path.append(setScriptDir)

importMayaScript("exempleMaya")      
from Terrain_hexagon_gen import terrain

terrain()
