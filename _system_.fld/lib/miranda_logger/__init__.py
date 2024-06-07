from datetime import datetime
import os
import sys
import re


def parent(directory=os.getcwd(), levels=1):
    parent_dir = os.path.abspath(os.path.join(directory, *([os.pardir] * levels)))
    return parent_dir


sys.path.append(parent())
import miranda_folder  # noqa


def log(action, description):
    id_path = os.path.join(miranda_folder.root(), "_system_.fld", "libdata", "miranda", "ID.var")
    id_ = int(open(id_path, "r").read())
    now = datetime.now()
    datetime_str = now.strftime("%d-%m-%Y %I:%M:%S%p")
    msg = f"[{action.upper()} - {id_:06}] @ [{datetime_str}] ~ {description.upper()}\n"
    path = os.path.join(miranda_folder.root(), "_logs_.fld", "_log_ID"+str(id_)+"_.log")
    with open(path, "a") as file:
        file.write(msg)


def clear(d=False):
    id_path = os.path.join(miranda_folder.root(), "_system_.fld", "libdata", "miranda", "ID.var")
    id_file = int(open(id_path, "r").read())
    path = os.path.join(miranda_folder.root(), "_logs_.fld")
    pattern = re.compile(r"_log_ID\d+_.log$")
    for filename in os.listdir(path):
        if pattern.match(filename) and filename != f"_log_ID{id_file}_.log":
            f_path = os.path.join(path, filename)
            fake_path = os.path.join("~", "_logs_.fld", filename)
            os.remove(f_path)
            log("INFO", "DELETED FILE: %s" % f_path)
            if d:
                print(":: Removed file: %s" % fake_path)
