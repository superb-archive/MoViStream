# Overview
- kafka-hackathon 실행을 위한 컨테이너 환경 구성

## Getting Started

1. container start
    ```bash
    cd docker

    docker-compose up 
    or
    docker-compose up -d
    ```
2. container status
    ```bash
    $ docker ps
    CONTAINER ID   IMAGE                                             COMMAND                  CREATED       STATUS       PORTS                                        NAMES
    404a1cd36568   confluentinc/cp-ksqldb-cli:7.1.1                  "/bin/bash -c 'echo …"   2 hours ago   Up 2 hours                                                ksqldb-cli
    e77173c2270d   confluentinc/cp-enterprise-control-center:7.1.0   "/etc/confluent/dock…"   2 hours ago   Up 2 hours   0.0.0.0:9021->9021/tcp                       control-center
    60b96f9c820e   confluentinc/cp-ksqldb-server:7.1.1               "/etc/confluent/dock…"   2 hours ago   Up 2 hours   0.0.0.0:8088->8088/tcp                       ksqldb-server
    5edb22b5b87e   confluentinc/cp-kafka:7.1.1                       "/etc/confluent/dock…"   2 hours ago   Up 2 hours   9092/tcp, 0.0.0.0:29092->29092/tcp           broker
    08521ea01733   confluentinc/cp-zookeeper:7.1.1                   "/etc/confluent/dock…"   2 hours ago   Up 2 hours   2888/tcp, 0.0.0.0:2181->2181/tcp, 3888/tcp   zookeeper
    ```
3. Topics 
    ```bash
    ❯ docker exec -it broker bash
    [appuser@broker ~]$ kafka-topics --bootstrap-server broker:9092 --list
    __consumer_offsets
    __transaction_state
    ```
4. Connect ksql cli
    ```bash
    ❯ docker exec -it ksqldb-cli ksql http://ksqldb-server:8088
    OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.

                      ===========================================
                      =       _              _ ____  ____       =
                      =      | | _____  __ _| |  _ \| __ )      =
                      =      | |/ / __|/ _` | | | | |  _ \      =
                      =      |   <\__ \ (_| | | |_| | |_) |     =
                      =      |_|\_\___/\__, |_|____/|____/      =
                      =                   |_|                   =
                      =        The Database purpose-built       =
                      =        for stream processing apps       =
                      ===========================================

    Copyright 2017-2021 Confluent Inc.

    CLI v7.1.1, Server v7.1.1 located at http://ksqldb-server:8088
    Server Status: RUNNING

    Having trouble? Type 'help' (case-insensitive) for a rundown of how things work!
    ```
5. Create table
    ```sql
    ksql> CREATE TABLE labels (id VARCHAR PRIMARY KEY, category VARCHAR, scene VARCHAR, timeofday VARCHAR, weather VARCHAR) WITH (KAFKA_TOPIC = 'labels', VALUE_FORMAT = 'JSON');

    Message
    ---------------
    Table created
    ---------------
    ksql> show tables;

    Table Name | Kafka Topic | Key Format | Value Format | Windowed
    -----------------------------------------------------------------
    LABELS     | labels      | KAFKA      | JSON         | false
    -----------------------------------------------------------------
    ```
6. Control Center
- open http://localhost:9092 in a browser.
- monitoring Bokers, Topics, ksqlDB, Consumers etc..