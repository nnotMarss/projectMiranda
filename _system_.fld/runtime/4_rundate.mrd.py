import sys, os
from datetime import datetime
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
now = datetime.now()
datetime_str = now.strftime("%d-%m-%Y %I:%M:%S%p")
file_path = os.path.join(os.getcwd(), "_system_.fld", "libdata", "miranda", "RUNDATE.var")
with open(file_path, 'r+') as f:
    if f.read() == "" or f.read() is None:
        f.write(datetime_str)
    pass
log("INFO", "%s: RUNTIME 4 SUCCESSFUL" % name)
