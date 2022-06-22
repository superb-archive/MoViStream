import json

from ksql import KSQLAPI


def get_accelerometer_index(filter_query="") -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query("SELECT x,y,z FROM accelerometer_query" + filter_query)

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict


def get_gps_index(filter_query="") -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query(
        "SELECT LONGITUDE, LATITUDE FROM locations_query" + filter_query
    )

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict


def get_category_index(filter_query="") -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query("SELECT * FROM category_index")

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict


def get_scene_index(filter_query="") -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query("SELECT * FROM scene_index")

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict


def get_weather_index(filter_query="") -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query("SELECT * FROM weather_index")

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict


def get_timeofday_index(filter_query="") -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query("SELECT * FROM timeofday_index")

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict


def get_random_10_vehicles() -> list:
    client = KSQLAPI("http://localhost:8088")
    query = client.query("SELECT * FROM label_count LIMIT 10;")

    results = []

    while True:
        try:
            result = next(query)
            results.append(result)
        except RuntimeError:
            break

    concat_result = "".join(results)
    result_dict = json.loads(concat_result)
    return result_dict
