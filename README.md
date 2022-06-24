# MoViStream

Submission for Kafka Summit Hackathon 2022

---

## Overview

MoViStream is an end-to-end platform for monitoring and visualizing sensor data streams from smart vehicles.

### Why smart vehicles?

- Modern vehicles utilize various sensors (ex, gps, IMU, camera) to understand scenes (ex, autonomous driving).

- This sensor data is valuable for controlling & monitoring other city infrastructures (ex, smart traffic lights).

- The rich data can be used for training centralized ML models that are deployed to vehicles (i.e. federated learning).

### Why Kafka & KSQL?

- Real-time sensor data from smart vehicles have very high volume and frequency, which requires a robust event-streaming technology.

- Live monitoring as well as machine learning experiments require data to be stored and processed into various forms, on-demand.

### Components

The subdirectories represent parts of the end-to-end platform, each equipped with a detailed description in their respective README files. Following is a brief summary of each component.


| Component | Description                                               |
| --------- | --------------------------------------------------------- |
| data      | driving dataset samples from BDD100k & preparation script |
| docker    | docker-compose & ksql init script                         |
| frontend  | streamlit application used for data visualization         |
| simulator | a lightweight python script for producing data streams    |

## Usage

### Requirements

This project has been developed and tested in the following environment. Note there could be issues when launching the app in other environments (OS, CPU architecture).

- macOS or ubuntu 18.04 on Intel CPU & 16GB RAM
- docker-compose, python 3.9, pipenv (version 2020.11.15)

### Getting Started

<<<<<<< Updated upstream
Below instructions guide you through the end-to-end steps for running MoViStream.
=======
Instructions below will guide you through the steps of running MobiStream.
>>>>>>> Stashed changes

1. docker setup

    Run below command to install and run kafka, ksqldb(ksql), etc. as docker containers in background.

    ```sh
    $ docker-compose -f docker/docker-compose.yaml up -d
    ```

    - Details of the containers are documented [here](./docker/README.md).

2. install dependencies

    Run below command to install necessary python dependencies (confluent-kafka, ksql, streamlit, etc).

    ```sh
    $ pipenv install
    $ pipenv shell
    ```

3. run simulator

    Below command starts up our vehicle simulator with data samples from the state-of-the-art [BDD100k](https://www.bdd100k.com/) dataset.

    ```sh
    $ python simulator/main.py --data=demo
    ```

    - Instructions on experimenting with the original source data is documented [here](./data/README.md)
    - Details of the simulator are documented [here](./simulator/README.md).

4. run dashboard

    ```sh
    $ cd frontend
    $ streamlit run streamlit.py
    ```

    - Explanations on visualized data are documented [here](./frontend/README.md).
