# Kafka python client

## Confluent Cloud setting

```bash
# set path
$ export PYTHONPATH=.
```

### Install Python dependencies

install python package using pipenv

```bash
$ PIPENV_VENV_IN_PROJECT=true pipenv install --python 3.8.12 --dev
```

### Install Python dependencies in mac m1

install `librdkafka` (**only for mac M1**)

```bash
$ cd ~ && mkdir tmp && cd tmp
$ git clone https://github.com/edenhill/librdkafka.git
$ cd librdkafka
$ ./configure --install-deps
$ brew install  openssl zstd pkg-config
$ ./configure
$ make
$ sudo make install
```

install python package using pipenv

```bash
$ PIPENV_VENV_IN_PROJECT=true pipenv install --python 3.8.12 --dev
```

### Activate virtual environment

```bash
$ pipenv shell
```

### run kafka producer

```bash
$ ./src/producer.py -f ./confluent/python.config -t test1
```

### run kafka consumer

```bash
$ ./src/consumer.py -f ./confluent/python.config -t test1
```

### run streamlit

```bash
$ streamlit run src/streamlit/visualizer.py
```
