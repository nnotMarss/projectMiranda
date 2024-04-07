import os
import sys
import subprocess

def parent(dir=os.getcwd(), levels=1):
    """
    Returns the absolute path of the parent dir.
    :param dir: Current dir. Defaults to the current working dir.
    :param levels: Number of levels to go up in the dir hierarchy. Defaults to 1.
    :return: Absolute path of the parent dir.
    """
    parentDir = os.path.abspath(os.path.join(dir, *([os.pardir] * levels)))
    return parentDir

def addToPath(levels=1):
    """
    Adds the parent dir to sys.path.
    :param levels: Number of levels to go up in the dir hierarchy. Defaults to 1.
    """
    parentDir = parent(levels=levels)
    sys.path.append(parentDir)

def root():
    """
    Returns the path to the root dir.
    :param parentDir: Parent dir path.
    :return: Path to the root dir.
    """
    with open(os.path.join(".\\_system_.fld", "var", "ROOT.var"), "r") as f:
        rootP = f.read()
    return rootP

addToPath()
import mars_file  # noqa: E402
import miranda_log # noqa: E402

def getMeta(path: str, isCfg: bool, entry: str):
    """
    Retrieves meta information.
    :param path: Path to the folder.
    :param isCfg: Indicates whether it's a config file.
    :param entry: Entry name.
    :return: Tuple containing folder path, existence of __FOLDER__.mfc, and meta information.
    """
    # if not all((path, isCfg, entry)):
    #     raise TypeError("\n   -!!!-\n   [ERROR]: CANNOT BE EMPTY\n   -!!!-")
    path = os.path.join(path, '')
    folderMfcPath = os.path.join(path, "__FOLDER__.mfc")
    if not os.path.exists(folderMfcPath):
        raise RuntimeError("\n   -!!!-\n   [ERROR]: __FOLDER__.MFC FILE IS NOT PRESENT\n   -!!!-")
    mfcFileType = "miranda.folder.cfg" if isCfg else "miranda.folder.dsp"
    out = mars_file.lookUp._(folderMfcPath, mfcFileType, entry)
    if out is None:
        raise TypeError("\n   -!!!-\n   [ERROR]: INVALID ENTRY NAME\n   -!!!-")

    return path, os.path.exists(folderMfcPath), out

def runAll(dir):
    files = os.listdir(dir)
    pyFiles = sorted([f for f in files if f.endswith('.py')])
    
    for fN in pyFiles:
        fP = os.path.join(dir, fN)
        subprocess.run(['py', fP])
