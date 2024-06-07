import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
import miranda_folder as f  # noqa
if len(sys.argv) > 1:
    args = sys.argv[1].split()
with open(os.path.join(f.root(), "_system_.fld", "libdata", "miranda_versioncontrol", "VERSION.var"), 'r') as ver:
    ver = ver.read().split()
print(":: Version: %s\n:: Build: %s\n:: Version Codename: %s" % (ver[0], ver[2], ver[3]))