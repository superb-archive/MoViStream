# Datasets for autonomous vehicle simulation

## BDD100k

### Overview

BDD100K is a diverse driving dataset for heterogeneous multitask learning.
Since the dataset is very large, 5 data points have been sampled for demo.
You can download it in its entirety following the below instructions.

### Instructions

option1)
You can download our preprocessed version from [this gdrive](https://drive.google.com/drive/folders/1ASECOtBbbxVN8aWakvUunIH_9kbjpm7K?usp=sharing).

  1. Download and unzip the zip files as they were saved in gdrive.
  2. Afterwards, your folder tree should look something like below.

        ```sh
        BDD100k
        ├── labels
        │   ├── demo    # contains 5 json files
        │   ├── train   # contains 70k json files
        │   └── val     # contains 10k json files
        └── info
            ├── demo    # contains 5 json files
            ├── train   # contains 70k json files
            └── val     # contains 10k json files
        ```

option2)
The original dataset is also available at [bdd100k](https://doc.bdd100k.com/download.html).
Download the [labels](https://doc.bdd100k.com/download.html#labels) and [info](https://doc.bdd100k.com/download.html#info).
For preprocessing the labels, use to the `prepare_simulation_data.py` script.
