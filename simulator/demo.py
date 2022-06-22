import json
import os
from multiprocessing import Pool
from typing import List

from model import Image, Info, LabelFlattened
from node import Node

DATA_ROOT = "../data"
DATA_DIR = "demo"

POOL_SIZE = 2
CONCURRENCY = 4


def simulate_node(args):
    node = Node(args["conf"])
    node.produce_labels(args["labels"])
    node.produce_info(args["info"])


def fetch_labels(file_name: str):
    # image labels
    with open(f"{DATA_ROOT}/{DATA_DIR}/images/{file_name}", "r") as rf:
        image_dict = json.loads(rf.read())
        image = Image(**image_dict)
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

    return labels


def fetch_info(file_name: str):
    # sensor data
    with open(f"{DATA_ROOT}/{DATA_DIR}/info/{file_name}") as rf:
        info_dict = json.loads(rf.read())
        info = Info(**info_dict)

    return info


if __name__ == "__main__":
    conf = {"bootstrap.servers": "localhost:29092"}
    jobs: List[dict] = []

    file_name_list = os.listdir(f"{DATA_ROOT}/{DATA_DIR}/images")
    for file_name in file_name_list:
        print(file_name)
        try:
            labels = fetch_labels(file_name=file_name)
            info = fetch_info(file_name=file_name)
            args = {"conf": conf, "labels": labels, "info": info}
            jobs.append(args)
        except Exception:
            pass

        if len(jobs) == CONCURRENCY:
            with Pool(POOL_SIZE) as p:
                p.map(simulate_node, jobs)
            jobs = []

    if len(jobs):
        with Pool(POOL_SIZE) as p:
            p.map(simulate_node, jobs)
        jobs = []
