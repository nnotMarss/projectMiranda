import sys, os
name = os.path.basename(__file__)
args = []
if len(sys.argv) > 1:
    args = sys.argv[1].split()
if "-d" in args:
    print(":: %s" % str(" ".join(args)))
if "-h" in args:
    print("--%s HELP PANEL--\n:: This function is a dummy function,\n:: serving no function but to show how MIRANDA functions work." % (name.upper()))