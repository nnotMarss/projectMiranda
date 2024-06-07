import os
import sys
import subprocess
import difflib


def parent(directory=os.getcwd(), levels=1):
    parent_dir = os.path.abspath(os.path.join(directory, *([os.pardir] * levels)))
    return parent_dir


sys.path.append(parent())
import miranda_folder as folder  # noqa
from miranda_logger import log  # noqa


def find_similar(dir_: str, func: str) -> list:
    files = os.listdir(dir_)
    cmds = sorted([f for f in files if f.endswith('.pyi')])
    cmds = [command[:-4].upper() for command in cmds]
    return difflib.get_close_matches(func.upper(), cmds)


def run_func(func: str, args: list):
    func = func.lower()
    if func == "exit.mrd.pyi":
        log("WARN", "EXIT CODE: "+str(" ".join(args)).upper())
        sys.exit()
    var_dir = os.path.join(folder.root(), "_system_.fld", "var", "")
    func_path = os.path.join(var_dir, func.lower())
    if os.path.exists(func_path) is True:
        subprocess.run(['py', func_path, " ".join(args)])
    else:
        if func[:-8] is None or func[:-8] == "":
            pass
        else:
            print(":: No such function named '%s'!" % func[:-8])
            sug = find_similar(os.path.join(folder.root(), "_system_.fld", "var", ""), func)
            if sug:
                print(":: Did you mean %s?" % ", ".join(sug).lower()[:-4])
            else:
                pass


def run(func: str, args: list):
    if os.path.exists(func):
        subprocess.run(['py', func, " ".join(args)])
    else:
        print(":: No such file named '%s'!" % func)

