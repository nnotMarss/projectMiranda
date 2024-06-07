import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
if len(sys.argv) > 1:
    args = sys.argv[1].split()
from miranda_logger import log  # noqa
log("INFO","%s: TERMINAL FACE CLEARED" % name)
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
if "-D" in args:
    print(":: Screen cleared.")