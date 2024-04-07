import sys
import os
def parent(c = os.getcwd()):
    p = os.path.abspath(os.path.join(c, os.pardir))
    return p    
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib"))
from miranda_log import log  # noqa: E402
with open(os.path.join(os.getcwd(),"_system_.fld", "var", "ROOT.var"), "w") as f:
    f.write(os.path.join(os.getcwd(), ''))
    log("info","runtime 2 successful")