import random
import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib"))
idd = str(random.randint(100000, 999999))
with open(os.path.join(os.getcwd(), "_system_.fld", "libdata", "miranda", "ID.var"), 'w') as f:
    f.write(idd)
from miranda_logger import log  # noqa
log("info", "%s: runtime 1 successful" % name)