import json
import os
from multiprocessing import Pool
from typing import List

from cli import args
from model import Image, Info, LabelFlattened, LocationFlattened
from node import Node

DATA_ROOT = "../data/BDD100k"

DATA_DIR = args.data
if DATA_DIR not in ["demo", "train", "val"]:
    print("data path needs to be one of demo/train/val")
    exit()

POOL_SIZE = 2
CONCURRENCY = 10


def simulate_node(args):
    node = Node(args["conf"])
    node.produce_labels(args["labels"])
    node.produce_locations(args["locations"])


def fetch_labels(file_name: str):
    # image labels
    with open(f"{DATA_ROOT}/labels/{DATA_DIR}/{file_name}", "r") as rf:
        image_dict = json.loads(rf.read())
        image = Image(**image_dict)
        labels = [
            LabelFlattened(
                image_id=file_name,
                id=f"{file_name}#{label.id}",
                category=label.category,
                scene=image.attributes.scene,
                timeofday=image.attributes.timeofday,
                weather=image.attributes.weather,
            )
            for label in image.labels
        ]

    return labels


def fetch_locations(file_name: str):
    # sensor data
    with open(f"{DATA_ROOT}/info/{DATA_DIR}/{file_name}") as rf:
        info_dict = json.loads(rf.read())
        info = Info(**info_dict)
        locations = [
            LocationFlattened(
                id=f"{file_name}#{i}", image_id=file_name, **location.dict()
            )
            for i, location in enumerate(info.locations)
        ]

    return locations


if __name__ == "__main__":
    conf = {"bootstrap.servers": "localhost:29092"}
    jobs: List[dict] = []

    file_name_list = os.listdir(f"{DATA_ROOT}/labels/{DATA_DIR}")
    # while True:
    for file_name in file_name_list:
        try:
            labels = fetch_labels(file_name=file_name)
            locations = fetch_locations(file_name=file_name)
            args = {"conf": conf, "labels": labels, "locations": locations}
            jobs.append(args)
        except Exception as e:
            # print(file_name)
            pass

        if len(jobs) == CONCURRENCY:
            with Pool(POOL_SIZE) as p:
                p.map(simulate_node, jobs)
            jobs = []

    if len(jobs):
        with Pool(POOL_SIZE) as p:
            p.map(simulate_node, jobs)
        jobs = []
