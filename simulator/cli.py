import argparse

parser = argparse.ArgumentParser(description="CLI arguments for simulator.")
parser.add_argument(
    "-d",
    "--data",
    type=str,
    help="Sub-directory in which the json files are saved. (default = demo)",
)

args = parser.parse_args()
