import json
from multiprocessing import Pool
from typing import List

import ijson

from model import Image, Info, LabelFlattened
from node import Node

DATA_DIR = "data_demo"
# DATA_DIR = "data"  # uncomment this line to test with real data
POOL_SIZE = 2
CONCURRENCY = 10


def simulate_node(args):
    node = Node(args["conf"])
    node.produce_labels(args["labels"])
    node.produce_info(args["info"])


def parse_image(image_dict: dict):
    image = Image(**image_dict)
    image_id = image.name.replace("jpg", "json")

    # image labels
    labels = [
        LabelFlattened(
            id=f"{image.name}#{label.id}",
            category=label.category,
            scene=image.attributes.scene,
            timeofday=image.attributes.timeofday,
            weather=image.attributes.weather,
        )
        for label in image.labels
    ]

    # sensor data
    with open(f"../{DATA_DIR}/info/100k/val/{image_id}") as rf:
        info_dict = json.loads(rf.read())
        info = Info(**info_dict)

    return labels, info


if __name__ == "__main__":
    conf = {"bootstrap.servers": "localhost:29092"}

    while True:
        with open(f"../{DATA_DIR}/labels/bdd100k_labels_images_val.json") as rf:
            data = ijson.items(rf, "item")
            jobs: List[dict] = []
            for image_dict in data:
                if len(jobs) == CONCURRENCY:
                    with Pool(POOL_SIZE) as p:
                        p.map(simulate_node, jobs)
                    jobs = []

                try:
                    labels, info = parse_image(image_dict=image_dict)
                    args = {"conf": conf, "labels": labels, "info": info}
                    jobs.append(args)
                except Exception:
                    pass

            if len(jobs):
                with Pool(POOL_SIZE) as p:
                    p.map(simulate_node, jobs)
                jobs = []
