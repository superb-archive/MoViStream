import json
import time
from typing import List

from confluent_kafka import Producer

from cli import args
from model import AccelerometerFlattened, Image, Info, LabelFlattened, LocationFlattened

DATA_ROOT = "../data/BDD100k"

DATA_DIR = args.data
if DATA_DIR not in ["demo", "train", "val"]:
    print("data path needs to be one of demo/train/val")
    exit()


def fetch_labels(file_name: str):
    # image labels
    try:
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
    except Exception:
        labels = []

    return labels


def fetch_locations(file_name: str):
    # sensor data
    try:
        with open(f"{DATA_ROOT}/info/{DATA_DIR}/{file_name}") as rf:
            info_dict = json.loads(rf.read())
            info = Info(**info_dict)
            locations = [
                LocationFlattened(
                    id=f"{file_name}#{i}", image_id=file_name, **location.dict()
                )
                for i, location in enumerate(info.locations)
            ]
    except Exception:
        locations = []
    return locations


def fetch_accelerometer(file_name: str):
    # sensor data
    try:
        with open(f"{DATA_ROOT}/info/{DATA_DIR}/{file_name}") as rf:
            info_dict = json.loads(rf.read())
            info = Info(**info_dict)
            accelerometer = [
                AccelerometerFlattened(
                    id=f"{file_name}#{i}", image_id=file_name, **accel.dict()
                )
                for i, accel in enumerate(info.accelerometer)
            ]
    except Exception:
        accelerometer = []
    return accelerometer


class Node:
    def __init__(self, conf, file_name) -> None:
        self.producer = Producer(conf)
        self.labels: List[LabelFlattened] = fetch_labels(file_name=file_name)
        self.locations: List[LocationFlattened] = fetch_locations(file_name=file_name)
        self.accelerometer: List[AccelerometerFlattened] = fetch_accelerometer(
            file_name=file_name
        )

    def produce_labels(self):
        for label in self.labels:
            self.producer.produce(
                topic="labels",
                value=json.dumps(label.dict()),
                key=label.id,
            )
            self.producer.flush()
            time.sleep(40 / len(self.labels))

    def produce_locations(self):
        for location in self.locations:
            self.producer.produce(
                topic="locations",
                value=json.dumps(location.dict()),
                key=location.id,
            )
            self.producer.flush()
            time.sleep(40 / len(self.locations))

    def produce_accelerometer(self):
        for accel in self.accelerometer:
            self.producer.produce(
                topic="accelerometer",
                value=json.dumps(accel.dict()),
                key=accel.id,
            )
            self.producer.flush()
            time.sleep(40 / len(self.accelerometer))
