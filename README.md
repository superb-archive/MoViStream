# Autonomous Vehicle Intelligence

## Getting Started

1. docker setup

    ```sh
    $ docker-compose -f docker/docker-compose.yml up -d
    $ docker exec -it ksqldb-server bash
    ksql> [COPY tables.sql here]
    ```

2. install dependencies

    ```sh
    $ pipenv install
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