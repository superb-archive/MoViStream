# Autonomous Vehicle Intelligence

## Getting Started

1. docker setup

    ```sh
    $ docker-compose -f docker/docker-compose.yaml up -d
    $ docker exec -it broker bash -c "kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --topic labels --replication-factor 1 --partitions 1"
    $ docker exec -it broker bash -c "kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --topic info --replication-factor 1 --partitions 1"
    $ docker exec -it ksqldb-server bash
    ksql> [COPY tables.sql here]
    ```

2. install dependencies

    ```sh
    $ pipenv install
    $ pipenv shell
    ```

3. run simulator

    ```sh
    $ cd simulator
    $ python main.py
    ```

4. check messages
   ```sh
   $ docker exec -it broker bash -c "kafka-console-consumer --bootstrap-server localhost:9092 --topic labels --from-beginning"
   $ docker exec -it broker bash -c "kafka-console-consumer --bootstrap-server localhost:9092 --topic info --from-beginning"
   ```

5. run dashboard

    ```sh
    $ cd frontend
    $ streamlit run streamlit.py
    ```