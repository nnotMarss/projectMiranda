import sys, os
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
_json_posts_ = {
    "post1": {
        "title": "Test 1",
        "content": {
            "body1": "some textttt",
            "body2": "more texttt",
            "body3": "more textt",
            "body4": "more text",
            # [...]
        },
        "author": "m4rs_fox",
    },
    "post2": {
        "title": "Fuck me",
        "content": {
            "body1": "wtfff",
            "body2": "what am i doing here",
            "body3": " ",
            "body4": "lol, a space",
            # [...]
        },
        "author": "m4rs_fox",
    },
    "post3": {
        "title": "i wanna die",
        "content": {
            "body1": "python makes me wanna kms",
        },
        "author": "m4rs_fox",
    },
    "post4": {
        "title": "scream",
        "content": {
            "body1": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        },
        "author": "m4rs_fox",
    },
    "post69": {
        "title": "69 daddy fuck me harder! ahh~~",
        "content": {
            "body1": "very",
            "body2": "big",
            "body3": "dick"
        },
        "author": "m4rs_fox",
    },
}

new_arg = []
try:
    new_arg = args[0].split(":")
except IndexError:
    pass

if '-P' in new_arg:
    try:
        print(":: Post ID: " + new_arg[1])
        print(":: Post title: " + _json_posts_["post" + str(new_arg[1])]["title"])
        couner_body = 1
        print(":: Post Content:")
        try:
            while True:
                print(" : " + _json_posts_["post" + str(new_arg[1])]["content"]["body" + str(couner_body)])
                couner_body = couner_body + 1
        except KeyError:
            pass
        print(":: Author: @" + _json_posts_["post" + str(new_arg[1])]["author"])
        print("")
    except KeyError:
        print(":: Post with number '%s' wasn't found!" % new_arg[1])
else:
    counter = 1
    while True:
        try:
            print(":: Post ID: "+str(counter))
            print(":: Post title: " + _json_posts_["post" + str(counter)]["title"])
            print(":: Post Content:")
            couner_body = 1
            try:
                while True:
                    print(" : " + _json_posts_["post" + str(counter)]["content"]["body"+str(couner_body)])
                    couner_body = couner_body + 1
            except KeyError:
                pass
            print(":: Author: @"+_json_posts_["post"+str(counter)]["author"])
            counter = counter + 1
            print("\n")
        except KeyError:
            print("\n:: That's everything.")
            break