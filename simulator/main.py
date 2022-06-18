import json
import os
import time
from multiprocessing import Pool
from typing import List

import ijson

from model import Image, Info, LabelFlattened
from node import Node


def simulate_node(args):
    print("simulating node")
    node = Node(args["conf"])
    node.produce_labels(args["labels"])
    node.produce_info(args["info"])


def parse_image(image: Image):
    image_id = image.name.replace("jpg", "json")

    # image's labels
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

    # image's info
    with open(os.path.join(info_dir, image_id)) as rf:
        info_dict = json.loads(rf.read())
        info = Info(**info_dict)

    return labels, info


if __name__ == "__main__":
    conf = {"bootstrap.servers": "localhost:29092"}

    info_dir = "info"

    while True:
        with open("labels/bdd100k_labels_images_val.json") as rf:
            data = ijson.items(rf, "item")
            jobs: List[dict] = []
            for image_dict in data:
                # batch 2
                if len(jobs) == 2:
                    with Pool(2) as p:
                        p.map(simulate_node, jobs)
                    jobs = []
                    time.sleep(2)

                image = Image(**image_dict)
                labels, info = parse_image(image=image)
                args = {"conf": conf, "labels": labels, "info": info}
                jobs.append(args)

            if len(jobs):
                with Pool(2) as p:
                    p.map(simulate_node, jobs)
                jobs = []
                time.sleep(2)
