import sys
from omg import *

# check for command line arguments
if len(sys.argv) != 3:
    print("Incorrect number of arguments! Run by typing:")
    print("python3 wadparser.py <wadfile> <dumpfile>")
    print("Example:")
    print("python3 wadparser.py doom2.wad findings.txt")
    sys.exit(1)

# reads flag data
flag_file = open("flag.dat", "rb")
flag = flag_file.read()
flag_file.close()

# opens WAD file
wadfile = sys.argv[1]
dumpfile = sys.argv[2]
wad = WAD(wadfile)

# search for flag in WAD file
with open(dumpfile, "a") as dump:
    lumps = dict(wad.data)
    lumps.update(wad.patches)
    lumps.update(wad.graphics)
    
    for name, lump in lumps.items():
        if flag == lump.data:
            print("Flag found in lump {} of {}".format(name, wadfile))
            finding = "{},{}\n".format(wadfile, name)
            dump.write(finding)

