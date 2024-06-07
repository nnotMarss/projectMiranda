import random
import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa

pass
log("INFO", "%s: RUNTIME 5 SKIPPED" % name)
