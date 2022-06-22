import os
from multiprocessing import Pool
from threading import Thread
from typing import List

from cli import args
from node import Node

DATA_ROOT = "../data/BDD100k"

DATA_DIR = args.data
if DATA_DIR not in ["demo", "train", "val"]:
    print("data path needs to be one of demo/train/val")
    exit()

POOL_SIZE = 16
CONCURRENCY = 10


def simulate_node(args):
    node = Node(args["conf"], args["file_name"])
    thread1 = Thread(target=node.produce_labels)
    thread2 = Thread(target=node.produce_locations)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    conf = {"bootstrap.servers": "localhost:29092"}
    jobs: List[dict] = []

    file_name_list = os.listdir(f"{DATA_ROOT}/labels/{DATA_DIR}")
    # while True:
    for file_name in file_name_list:
        try:
            args = {"conf": conf, "file_name": file_name}
            jobs.append(args)
        except Exception as e:
            # print(file_name)
            e

        if len(jobs) == CONCURRENCY:
            with Pool(POOL_SIZE) as p:
                p.map(simulate_node, jobs)
            jobs = []

    if len(jobs):
        with Pool(POOL_SIZE) as p:
            p.map(simulate_node, jobs)
        jobs = []
