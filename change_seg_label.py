import os

import SimpleITK as sitk
import numpy as np


def copy_BraTS_segmentation_and_convert_labels(in_file, out_file):
    # use this for segmentation only!!!
    # nnUNet wants the labels to be continuous. BraTS is 0, 1, 2, 4 -> we make that into 0, 1, 2, 3
    img = sitk.ReadImage(in_file)
    img_npy = sitk.GetArrayFromImage(img)

    uniques = np.unique(img_npy)
    for u in uniques:
        if u not in [0, 1, 2, 3]:
            raise RuntimeError('unexpected label')

    seg_new = np.zeros_like(img_npy)
    seg_new[img_npy == 3] = 4
    seg_new[img_npy == 1] = 2
    seg_new[img_npy == 2] = 1
    img_corr = sitk.GetImageFromArray(seg_new)
    img_corr.CopyInformation(img)
    sitk.WriteImage(img_corr, out_file)


if __name__ == '__main__':
    """ change label from 0,1,2,3 to 0,1,2,4 """
    # because nnUNet wants the labels to be continuous. BraTS is 0, 1, 2, 4 -> we make that into 0, 1, 2, 3

    pred_path = '/datasets/pred'

    for p in os.listdir(pred_path):
        if '.nii.gz' in p:
            patdir = os.path.join(pred_path, p)
            copy_BraTS_segmentation_and_convert_labels(patdir, os.path.join(pred_path, 'seg_' + p[:-7] + ".nii.gz"))
            print(os.path.join(pred_path, 'seg_' + p[:-7] + ".nii.gz"))
