import os, numpy as np
from PIL import Image
from scipy import ndimage

SRC = "/home/claude/av"

def analyse(name):
    """Returns (grey array, label array, ordered region ids, bbox of artwork)."""
    a = np.array(Image.open(os.path.join(SRC, name + ".png")).convert("L"))
    white = a > 200
    lab, n = ndimage.label(white)
    border = set(lab[0,:]) | set(lab[-1,:]) | set(lab[:,0]) | set(lab[:,-1])
    border.discard(0)
    ink = ~white
    ys, xs = np.where(ink)
    floor = ((ys.max()-ys.min())*(xs.max()-xs.min())) * 0.0015
    regs = []
    for i in range(1, n+1):
        if i in border: continue
        s = int((lab == i).sum())
        if s >= floor:
            cy, cx = ndimage.center_of_mass(lab == i)
            regs.append({"id": i, "size": s, "cx": float(cx), "cy": float(cy)})
    regs.sort(key=lambda r: -r["size"])
    for k, r in enumerate(regs, 1):
        r["n"] = k
    return a, lab, regs, (ys.min(), ys.max(), xs.min(), xs.max())

NAMES = sorted(f[:-4] for f in os.listdir(SRC) if f.endswith(".png"))
