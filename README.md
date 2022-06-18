# Autonomous Vehicle Intelligence

## Getting Started

1. docker setup

    ```sh
    $ docker-compose up -d -f docker/docker-compose.yml
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

4. run dashboard

    ```sh
    $ cd frontend
    $ python streamlit.py
    ```