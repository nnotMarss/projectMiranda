import sys, os, time
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
import miranda_folder as folder  # noqa
import miranda_language as lang  # noqa
import miranda_function as func
from miranda_logger import log  # noqa
locale = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), 'r').read()
if len(sys.argv) > 1:
    args = sys.argv[1].split()

try:
    if args[0][:2] != "!\\":
        print(":: Remember about '!\\' prefix.\n:: Running from ROOT directory.\n")
        arg = "!\\"+args[0]
        path = os.path.join(os.getcwd(), args[0])
    else:
        arg = args[0]
        path = os.path.join(os.getcwd(), args[0][2:])
    if "_system_.fld" not in path.split("\\"):
        if "-D" not in args:
            if "mrd" in arg[2:].split("."):
                log("ERROR", "%s: TRIED BOOTING MODULES!" % name)
                print(":: File protected by MFI System.")
                exit()
            elif "dbg" in arg[2:].split("."):
                log("ERROR", "%s: TRIED BOOTING DEBUG MODULES!" % name)
                print(":: File protected by MFI System.")
                exit()
        elif "-D" in args:
            print(":: Running these files is risky! Proceed with caution!")
    else:
        print(":: Directory protected by MFI System.")
        log("ERROR", "%s: TRIED BOOTING IN SYSTEM FOLDER!" % name)
        exit()

    if os.path.exists(path) and os.path.isfile(path):
        log("INFO", "%s: EXECUTED PATH '%s'" % (name, path))
        func.run(path, [])
    else:
        log("INFO", "%s: UNABLE TO EXECUTE '%s'" % (name, path))
        print(":: No such file on path '%s'!" % arg)
except IndexError:
    print(":: Provide a valid path as 1st argument.")