# Import script in maya python

How to import scripts and make your projets modular.
You can see my tutorial on my website 

## Sommaire
1. [Problematic](#Problematic)
2. [Maya and path not a good love storie](#Maya-and-path-not-a-good-love-storie)
3. [Solution](#Solution)


## Problematic

I want to import my script to my project, with this method the project will be more maintainable and we will be more efficient to split the code to different file.
Python have implement this features and you check the documentation <a href="https://docs.python.org/3/tutorial/modules.html" target="_blank" rel="nofollow">here</a>

So i use the documentation of python top import my script 

<a href="https://docs.python.org/3/tutorial/modules.html#more-on-modules" target="_blank" rel="nofollow">(modules)</a>
<strong>Project arborescence :</strong>  

```bash
└── project  
    ├── exemple1  
             ├── testFunction.py  
    ├── main.py  
```

Working on Vs code debug but not in maya

```python
from exemple1.testFunction import test

test()
```

![test path](/img/testimport1.gif)

## Maya and path not a good love storie

In maya when you import a script, the relative path is not taken into consideration. The path is ovewride by the path script of maya.
We can check it with the library *pathlib*

![test path](/img/testimport.gif)


## Solution 

First we must put our project scipt in the maya folder script. 
For me it's here :
```bash
C:/Users/Gilles/Documents/maya/2022/scripts
```

Then we must forced to the path of our project.


```python
import maya.cmds as cmds
import sys 

def importMayaScript(nameFolder):

    # allows to recover le path du folder scrit
    myScriptDir = cmds.internalVar(userScriptDir=True)
    setScriptDir = myScriptDir+'project/src/'+str(nameFolder)+'/'
    
    sys.path.append(setScriptDir) 
```

I use the library sys to add the path to my import library.

We will use this method to have the path of the scirpt folder:
<a href="https://download.autodesk.com/us/maya/2010help/CommandsPython/internalVar.html" target="_blank" rel="nofollow">Internal Var</a>


Then we use *sys.path.append(setScriptDir)* to append the module to our library project.

```python
importMayaScript("exemple1")      

from testFunction import test

test()
```

Now it's working !

Now we use our python files as components !
Example of use : 

![reel test](/img/reelTest.gif)
