import json
from typing import List

from confluent_kafka import Producer

from model import GPSFlattened, LabelFlattened


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

    def produce_gpss(self, gpss: List[GPSFlattened]):

        for gps in gpss:
            self.producer.produce(
                topic="gps",
                value=json.dumps(gps.dict()),
                key=gps.id,
            )
            self.producer.flush()
