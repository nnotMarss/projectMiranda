import sys, os, requests, random
name = os.path.basename(__file__)
args = []
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
import miranda_folder as folder  # noqa
import miranda_language as lang  # noqa
from miranda_logger import log  # noqa
locale = open(os.path.join(folder.root(), "_system_.fld", "libdata", "miranda", "LANGUAGE.var"), 'r').read()
if len(sys.argv) > 1:
    args = sys.argv[1].split()
log("WARN", "%s: DELETE THIS FUNCTION WHEN DONE TESTING!" % name)

try:
    response = requests.get("https://cdn.ntmrs.xyz/@API/MISC/ave.response")
    if response.status_code == 200:
        for text in response.text.split("."):
            text_int = random.randint(1, 10)
            if text_int == 10:
                print(text)
    else:
        print(":: died")
except requests.exceptions.ConnectionError:
    print(":: no connection")