# MobiStream

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-394/) [![version - 0.1](https://img.shields.io/badge/version-0.1-blue)](https://) [![contributor - 4](https://img.shields.io/badge/contributor-4-blue)](https://)

Submission for Kafka Summit Hackathon 2022

---

## Overview

MobiStream is an end-to-end platform for streaming, monitoring and visualizing sensor data from smart vehicles.

### Why smart vehicles?

- Modern vehicles utilize various sensors (ex, gps, IMU, camera) to understand scenes (ex, autonomous driving).

- This sensor data is valuable for controlling & monitoring other city infrastructure (ex, smart traffic lights).

- The rich data can be used for training centralized ML models that are deployed to vehicles (i.e. federated learning).

### Why Kafka & KSQL?

- Real-time sensor data from smart vehicles has very high volume and frequency, which requires a robust event-streaming technology.

- Live monitoring as well as machine learning experiments require that data is stored and processed into various forms, on-demand.

### Components

The subdirectories in the file tree are parts of the end-to-end platform, each equipped with a detailed description in repective README files. Following is a brief summary of each component.

| Component | Description                                               |
| --------- | --------------------------------------------------------- |
| data      | driving dataset samples from BDD100k & preparation script |
| docker    | docker-compose & ksql init script                         |
| frontend  | streamlit application used for data visualization         |
| simulator | a lightweight python script for producing data streams    |

## Usage

### Requirements

This project has been developed and tested in the following environment. Note that minor issues have been recorded while running the app in other environments

- macOS or ubuntu 18.04 on Intel CPU & 16GB RAM
- docker-compose, python 3.9, pipenv (version 2020.11.15)

### Getting Started

Below instructions guide you through the end-to-end steps for running MobiStream.

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

   - Instructions on experimenting with the original source data is documented [here](./simulator/README.md)
   - Details of the simulator are documented [here](./simulator/README.md).

4. run dashboard

   ```sh
   $ cd frontend
   $ streamlit run streamlit.py
   ```

   - Explanations on visualized data are documented [here](./frontend/README.md).

## Streamlit demo

### metadata

![](/image/pie-chart.gif)

### vehicle location in map

![](/image/map.gif)

### vehicle tracking

![](/image/tracking.gif)
