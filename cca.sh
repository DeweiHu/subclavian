#!/usr/bin/env bash
loadDir=/home/hud4/Desktop/subclavian/niftidata
saveDir=/home/hud4/Desktop/subclavian/cca
c3d=/home/hud4/tool/c3d-1.0.0-Linux-x86_64/bin/c3d

vol=$loadDir/vol_seg.nii.gz
vol_open=$saveDir/vol_open.nii.gz
vol_opt=$saveDir/vol_opt.nii.gz

$c3d $vol -erode 1 3x3x3vox -o $vol_open
$c3d $vol_open -dilate 1 3x3x3vox -o $vol_open
$c3d $vol_open -comp -o $vol_opt
