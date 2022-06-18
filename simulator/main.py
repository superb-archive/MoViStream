import json
import os
import time
from multiprocessing import Pool

import ijson
from confluent_kafka import Producer

from model import Image, Info, LabelFlattened
from node import Node


def simulate_node(conf):
    node = Node(conf)
    node.produce_label()
    node.produce_info()


if __name__ == "__main__":
    conf = {"bootstrap.servers": "localhost:29092"}

    with Pool(2) as p:
        while True:
            p.map(simulate_node, [conf])
            time.sleep(10)
