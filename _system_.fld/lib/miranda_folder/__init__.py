import os
import sys
import subprocess


def parent(dir_=os.getcwd(), levels=1):
    parent_dir = os.path.abspath(os.path.join(dir_, *([os.pardir] * levels)))
    return parent_dir


def add_path(levels=1):
    parent_dir = parent(levels=levels)
    sys.path.append(parent_dir)


def root():
    return open(os.path.join(".\\_system_.fld", "libdata", "miranda", "ROOTPATH.var"), "r").read()


add_path()
import mars_file  # noqa

# Outdated.
# def get_meta(path: str, isCfg: bool, entry: str):
#     # if not all((path, isCfg, entry)):
#     #     raise TypeError("\n   -!!!-\n   [ERROR]: CANNOT BE EMPTY\n   -!!!-")
#     path = os.path.join(path, '')
#     folder_mfc_path = os.path.join(path, "__FOLDER__.mfc")
#     if not os.path.exists(folder_mfc_path):
#         raise RuntimeError("\n   -!!!-\n   [ERROR]: __FOLDER__.MFC FILE IS NOT PRESENT\n   -!!!-")
#     folder_mfc_type = "miranda.folder.cfg" if isCfg else "miranda.folder.dsp"
#     out = mars_file.lookUp._(folder_mfc_path, folder_mfc_type, entry)
#     if out is None:
#         raise TypeError("\n   -!!!-\n   [ERROR]: INVALID ENTRY NAME\n   -!!!-")
#
#     return path, os.path.exists(folder_mfc_path), out


def run_all(dir_):
    files = os.listdir(dir_)
    py_files = sorted([f for f in files if f.endswith('.py')])
    
    for f_n in py_files:
        f_p = os.path.join(dir_, f_n)
        subprocess.run(['py', f_p])
