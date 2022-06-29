# This work is forked from [MAML](https://github.com/YaoZhang93/MAML)

# Modality-aware Mutual Learning for Multi-modal Medical Image Segmentation

## Usage

* Pytorch

```shell
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
```

* requirements

```shell
cd MAML
pip install -e .
```

* add datasets path

```shell
source init.sh
```

* Data Preparation

  - Download the data from synapse : [MICCAI 2021 BraTS Challenge](https://www.synapse.org/#!Synapse:syn27046444/wiki/616571).

  - Convert the datasets by

  `python nnunet/dataset_conversion/Task521_BraTS_2021.py`

  - Preprocess the datasets by

  `python nnunet/experiment_planning/nnUNet_plan_and_preprocess.py -t 521 --verify_dataset_integrity`

* Train

  - Train the model by

  `python nnunet/run/run_training.py 3d_fullres MAMLTrainerV2 521 0`

* Test

  - inference on the test data by

  `python nnunet/inference/predict_simple.py -i INPUT_PATH -o OUTPUT_PATH -t 521 -f 0 -tr MAMLTrainerV2`

## Citation

```
@inproceedings{zhang2021modality,
  title={Modality-Aware Mutual Learning for Multi-modal Medical Image Segmentation},
  author={Zhang, Yao and Yang, Jiawei and Tian, Jiang and Shi, Zhongchao and Zhong, Cheng and Zhang, Yang and He, Zhiqiang},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={589--599},
  year={2021},
  organization={Springer}
}
```

## Acknowledgement

`MAML` is integrated with the out-of-box [nnUNet](https://github.com/MIC-DKFZ/nnUNet).
