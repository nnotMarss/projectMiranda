import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
with open(os.path.join(os.getcwd(), "_system_.fld", "libdata", "miranda", "ROOTPATH.var"), "w") as f:
    f.write(os.path.join(os.getcwd(), ''))
    log("info", "%s: runtime 2 successful" % name)
