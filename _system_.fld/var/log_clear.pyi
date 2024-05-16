import sys, os
name = os.path.basename(__file__)
args = []
if len(sys.argv) > 1:
    args = sys.argv[1].split()
sys.path.append(os.path.join(os.getcwd(), "_system_.fld", "lib", ""))
import miranda_logger as ml  # noqa
print(args)
ml.clear(False if '-S' in args else True) #doesnt work for some reason?