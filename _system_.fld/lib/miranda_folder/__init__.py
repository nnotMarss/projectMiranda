import os
import sys
import subprocess


def parent(dir_=os.getcwd(), levels=1):
    """
    Returns the absolute path of the parent dir.
    :param dir_: Current dir. Defaults to the current working dir.
    :param levels: Number of levels to go up in the dir hierarchy. Defaults to 1.
    :return: Absolute path of the parent dir.
    """
    parent_dir = os.path.abspath(os.path.join(dir_, *([os.pardir] * levels)))
    return parent_dir


def add_path(levels=1):
    """
    Adds the parent dir to sys.path.
    :param levels: Number of levels to go up in the dir hierarchy. Defaults to 1.
    """
    parent_dir = parent(levels=levels)
    sys.path.append(parent_dir)


def root():
    """
    Returns the path to the root dir.
    :return: Path to the root dir.
    """
    with open(os.path.join(".\\_system_.fld", "var", "ROOT.var"), "r") as f:
        root_dir = f.read()
    return root_dir


add_path()
import mars_file  # noqa: E402


def get_meta(path: str, isCfg: bool, entry: str):
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
    folder_mfc_path = os.path.join(path, "__FOLDER__.mfc")
    if not os.path.exists(folder_mfc_path):
        raise RuntimeError("\n   -!!!-\n   [ERROR]: __FOLDER__.MFC FILE IS NOT PRESENT\n   -!!!-")
    folder_mfc_type = "miranda.folder.cfg" if isCfg else "miranda.folder.dsp"
    out = mars_file.lookUp._(folder_mfc_path, folder_mfc_type, entry)
    if out is None:
        raise TypeError("\n   -!!!-\n   [ERROR]: INVALID ENTRY NAME\n   -!!!-")

    return path, os.path.exists(folder_mfc_path), out


def run_all(dir_):
    files = os.listdir(dir_)
    py_files = sorted([f for f in files if f.endswith('.py')])
    
    for f_n in py_files:
        f_p = os.path.join(dir_, f_n)
        subprocess.run(['py', f_p])
