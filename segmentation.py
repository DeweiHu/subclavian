import sys
sys.path.insert(0,"/home/hud4/Desktop/phantom/")
import util
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import nibabel as nib

def thresh(rng,im):
    im[im <= rng[0]] = 0
    im[im >= rng[1]] = 0
    im[im > 0] = 1
    return im

data_dir = "/home/hud4/Desktop/subclavian/niftidata/"
save_dir = "/home/hud4/Desktop/subclavian/cca/"
vol_name = "pt2"
vol = util.nii_loader(data_dir+vol_name+".nii.gz")
data = nib.load(data_dir+vol_name+".nii.gz")
header = data.header

rng = [105,380]
h,w,nslc = vol.shape
vol_bin = np.zeros([h,w,nslc],dtype=np.int16)

# thresholding
for i in range(nslc):
    im = vol[:,:,i]
    vol_bin[:,:,i] = thresh(rng,im)

util.nii_saver(vol_bin,data_dir,"vol_seg.nii.gz")

#%%
sh_dir = "/home/hud4/tool/cca.sh"
subprocess.call(sh_dir)
vol_cca = util.nii_loader("/home/hud4/Desktop/subclavian/cca/vol_opt.nii.gz")

seg = np.uint8(vol_cca == 1)
util.nii_saver(seg, save_dir, "{}_seg.nii.gz".format(vol_name), header)
