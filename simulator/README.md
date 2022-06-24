# Vehicle Data Streams Simulator

## Dataset

We used BDD100k dataset to simulate multiple vehicles (i.e. nodes), by having each virtual vehicle process produce stream data to Kafka. The simulator sends on-device machine learning inference results (ex, labels) and vehicular sensor data (ex, location and velocity) to a kafka cluster (local / cloud).

## Instructions

1. install dependencies

    ```sh
    $ cd ..
    $ pipenv install
    $ pipenv shell
    ```

2. run simulator with various data volume

    - demo data (100)

        ```sh
        $ cd simulator
        $ python main.py --data demo
        ```

    - below two cases require [data download step](../data/README.md)

    - train set (70k)

        ```sh
        $ python main.py --data train
        ```

    - validation set (10k)

        ```sh
        $ python main.py --data val
        ```

3. check messages arrived at two topics

    - `labels`: ML inference results

        ```sh
        $ docker exec -it broker bash -c "kafka-console-consumer --bootstrap-server localhost:9092 --topic labels --from-beginning"
        ```

    - `info`  : vehicular sensor data

        ```sh
        $ docker exec -it broker bash -c "kafka-console-consumer --bootstrap-server localhost:9092 --topic info --from-beginning"
        ```
