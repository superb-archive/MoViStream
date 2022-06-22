import json
import os

DATA_DIR = "./BDD100k"

for split in ["train", "val"]:
    if not os.path.isfile(f"{DATA_DIR}/labels/bdd100k_labels_images_{split}.json"):
        print(f"move bdd100k_labels_images_{split}.json to {DATA_DIR}/labels")

    with open(f"{DATA_DIR}/labels/bdd100k_labels_images_{split}.json") as f:
        images = json.load(f)

    for image in images:
        image_id = image["name"].split(".jpg")[0]
        with open(f"{DATA_DIR}/labels/{split}/{image_id}.json", "w") as wf:
            wf.write(json.dumps(image))
