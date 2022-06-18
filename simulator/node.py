import json
import os
import time

import ijson
from confluent_kafka import Producer

from model import Image, Info, LabelFlattened


class Node:
    def __init__(self, conf) -> None:
        self.producer = Producer(conf)

    def produce_label(self):

        with open("labels/bdd100k_labels_images_val.json") as rf:
            data = ijson.items(rf, "item")
            for image_dict in data:
                image = Image(**image_dict)
                for label in image.labels:
                    label_flattened = LabelFlattened(
                        id=f"{image.name}#{label.id}",
                        category=label.category,
                        scene=image.attributes.scene,
                        timeofday=image.attributes.timeofday,
                        weather=image.attributes.weather,
                    )

                    self.producer.produce(
                        topic="labels",
                        value=json.dumps(label_flattened.dict()),
                        key=label_flattened.id,
                    )
                    self.producer.flush()

    def produce_info(self):

        directory = "info"
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if not os.path.isfile(f):
                continue
            with open(f) as rf:
                info_dict = json.loads(rf.read())
                info = Info(**info_dict)

                self.producer.produce(
                    topic="info",
                    value=json.dumps(info.dict()),
                    key=info.id,
                )
                self.producer.flush()
