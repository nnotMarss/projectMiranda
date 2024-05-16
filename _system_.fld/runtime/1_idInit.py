import random
import os
import sys
def parent(c = os.getcwd()):
    p = os.path.abspath(os.path.join(c, os.pardir))
    return p    
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib"))
id = str(random.randint(100000, 999999))
with open(os.path.join(os.getcwd(),"_system_.fld", "var", "ID.var"), 'w') as f:
    f.write(id)
from miranda_logger import log  # noqa: E402
log("info", "runtime 1 successful")