import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
import miranda_language as lang  # noqa
import miranda_folder as folder  # noqa
from miranda_feedback import e621_integration as e621  # noqa
if len(sys.argv) > 1:
    args = sys.argv[1]  # not using .split() is intended!!
locale = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), 'r').read()
log("WARN", "%s: DELETE THIS FUNCTION WHEN DONE TESTING!" % name)

e621.get_e621_post_random()

# try:
#     fb.send_message(args)
# except Exception as error:  # noqa
#     print(":: %s '%s'" % (lang.lang(locale, "feedback_fail_function"), error))