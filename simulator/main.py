import json
import time

import ijson
from confluent_kafka import Producer

from model import Image, LabelFlattened

conf = {"bootstrap.servers": "localhost:29092"}
producer = Producer(conf)

with open("bdd100k_labels_images_val.json") as rf:
    data = ijson.items(rf, "item")

    while True:
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

                producer.produce(
                    topic="labels",
                    value=json.dumps(label_flattened.dict()),
                    key=label_flattened.id,
                )

            time.sleep(5)
