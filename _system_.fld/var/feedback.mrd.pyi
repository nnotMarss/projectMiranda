import sys, os
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
from miranda_logger import log  # noqa
import miranda_language as lang  # noqa
import miranda_folder as folder  # noqa
import miranda_feedback as fb  # noqa
if len(sys.argv) > 1:
    args = sys.argv[1]  # not using .split() is intended!!
locale = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), 'r').read()

try:
    log("INFO", "%s: TRYING TO SEND FEEDBACK..." % name)
    fb.send_message(args)
    log("INFO", "%s: FEEDBACK SENT" % name)
except Exception as error:  # noqa
    print(":: %s '%s'" % (lang.lang(locale, "feedback_fail_function"), error))
    log("ERROR", "%s: ERROR '%s' DURING SENDING!" % (name, error))