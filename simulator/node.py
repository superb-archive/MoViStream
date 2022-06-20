import json
from typing import List

from confluent_kafka import Producer

from model import Info, LabelFlattened


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

    def produce_info(self, info: Info):

        self.producer.produce(
            topic="info",
            value=json.dumps(info.dict()),
            key=info.id,
        )
        self.producer.flush()
