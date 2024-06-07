import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
import miranda_folder as mf  # noqa
mf.run_all(os.path.join(mf.root(), "_system_.fld", "runtime", ""))
log("INFO", "%s: VAR TABLE UPDATED" % name)