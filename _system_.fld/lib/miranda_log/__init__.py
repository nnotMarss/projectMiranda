from datetime import datetime
import os
import sys
import re
def parent(directory=os.getcwd(), levels=1):
    parentDir = os.path.abspath(os.path.join(directory, *([os.pardir] * levels)))
    return parentDir
sys.path.append(parent())
import miranda_folder  # noqa: E402

def log(action, description):
    idPath = os.path.join(miranda_folder.root(), "_system_.fld", "var", "ID.var")
    id = int(open(idPath, "r").read())
    now = datetime.now()
    datetime_str = now.strftime("%d-%m-%Y %I:%M:%S%p")
    msg = f"[{action.upper()} - {id:06}] @ [{datetime_str}] ~ {description.upper()}\n"
    path = os.path.join(miranda_folder.root(), "_logs_.fld", "_log_ID"+str(id)+"_.log")
    with open(path, "a") as file:
        file.write(msg)

def clear(d=False):
    idPath = os.path.join(miranda_folder.root(), "_system_.fld", "var", "ID.var")
    id = int(open(idPath, "r").read())
    path = os.path.join(miranda_folder.root(), "_logs_.fld")
    pattern = re.compile(r"_log_ID\d+_.log$")
    for filename in os.listdir(path):
        if pattern.match(filename) and filename != f"_log_ID{id}_.log":
            fPath = os.path.join(path, filename)
            os.remove(fPath)
            log("INFO", "DELETED FILE: %s" % fPath)
            if d:
                print(":: REMOVED FILE: %s" % fPath) 