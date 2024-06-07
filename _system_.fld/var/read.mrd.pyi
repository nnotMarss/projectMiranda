import sys, os
args = []
name = os.path.basename(__file__)
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
if len(sys.argv) > 1:
    args = sys.argv[1].split()
from miranda_logger import log  # noqa
import miranda_folder as f  # noqa

try:
    fake_path = args[0]
    real_path = os.path.join(os.getcwd(), args[0])
    if args[0][:1] == "\\":
        fake_path = "!"+args[0]
    elif args[0][:1] != "!":
        fake_path = "!\\"+args[0]

    if args[0][:2] == "!\\":
        real_path = os.path.join(os.getcwd(), args[0][2:])
    elif args[0][:1] == "\\":
        real_path = os.path.join(os.getcwd(), args[0][1:])
    print(":: Reading file: %s" % fake_path)
    log("INFO", "%s: READING FILE '%s'!" % (name, real_path))
    with open(real_path, 'r') as file:
        print(file.read())
except IndexError:
    print(":: No file specified.")
    log("WARN","%s: NO FILE SPECIFIED" % name)
except FileNotFoundError:
    print(":: File doesn't exists.")
    log("WARN", "%s: FILE '%s' DOESN'T EXISTS" % (name, real_path))
finally:
    log("INFO", "%s: PROCESS EXITED" % name)
