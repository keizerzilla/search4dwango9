import sys
import numpy as np
from omg import *
from skimage.metrics import structural_similarity as ssim

def calculate_similarity(im1, im2):
    """
    """
    
    return ssim(im1, im2)

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

# flag image as numpy array
flag_gfx = Graphic(flag)
flag_img = np.array(flag_gfx.to_Image())

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
        try:
            gfx = Graphic(lump.data)
            img = np.array(gfx.to_Image())
            
            ans = calculate_similarity(flag_img, img)
            
            if abs(ans) >= 0.1:
                gfx.to_file(f"temp/{name}.bmp")
                print(name, ans)
        except:
            pass
        
        if flag == lump.data:
            print("Flag found in lump {} of {}".format(name, wadfile))
            finding = "{},{}\n".format(wadfile, name)
            dump.write(finding)
