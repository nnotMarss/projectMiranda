import os
import sys
import subprocess


def parent(directory=os.getcwd(), levels=1):
    parent_dir = os.path.abspath(os.path.join(directory, *([os.pardir] * levels)))
    return parent_dir


sys.path.append(parent())
import miranda_folder as folder  # noqa
from miranda_logger import log  # noqa


def run_func(func: str, args: list):
    if func == "exit.pyi":
        log("WARN", "EXIT CODE: "+str(" ".join(args)).upper())
        sys.exit()
    var_dir = os.path.join(folder.root(), "_system_.fld", "var", "")
    func_path = os.path.join(var_dir, func)
    if os.path.exists(func_path) is True:
        subprocess.run(['py', func_path, " ".join(args)])
    else:
        print(":: No such function '%s'!" % func[:-4])
