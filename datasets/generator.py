import json

with open("coco/annotations/person_keypoints_val2017.json") as f:

    data: dict = json.load(f)
    # print(data.keys())  # 'info', 'images', 'licenses', 'categories', 'annotations'
    # print(len(data["images"]))  # 5000
    # print(len(data["licenses"]))  # 8
    # print(len(data["categories"]))  # 80

for image in data["images"]:
    print(image)
