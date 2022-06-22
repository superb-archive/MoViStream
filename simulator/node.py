import json
from typing import List

from confluent_kafka import Producer

from model import LabelFlattened, LocationFlattened


class Node:
    def __init__(self, conf) -> None:
        self.producer = Producer(conf)

    def produce_labels(self, labels: List[LabelFlattened]):

        for label in labels:
            self.producer.produce(
                topic="labels",
                value=json.dumps(label.dict()),
                key=label.id,
            )
            self.producer.flush()

    def produce_locations(self, locations: List[LocationFlattened]):

        for location in locations:
            self.producer.produce(
                topic="locations",
                value=json.dumps(location.dict()),
                key=location.id,
            )
            self.producer.flush()
