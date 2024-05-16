from sys import path
import os
path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
import miranda_folder as mf
mf.run_all(os.path.join(mf.root(), "_system_.fld", "runtime", ""))