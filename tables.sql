CREATE TABLE labels (
    id VARCHAR PRIMARY KEY,
    image_id VARCHAR,
    category VARCHAR,
    scene VARCHAR,
    timeofday VARCHAR,
    weather VARCHAR
) WITH (
    KAFKA_TOPIC = 'labels',
    VALUE_FORMAT = 'JSON'
);

CREATE TABLE labels_query WITH (KEY_FORMAT = 'JSON') AS
SELECT
    *
FROM
    labels;

CREATE TABLE info (
    image_id VARCHAR PRIMARY KEY,
    timelapse INT,
    startTime INT,
    endTime INT
) WITH (
    KAFKA_TOPIC = 'info',
    VALUE_FORMAT = 'JSON'
);

CREATE TABLE info_query WITH (KEY_FORMAT = 'JSON') AS
SELECT
    *
FROM
    info;

CREATE TABLE category_index WITH (KEY_FORMAT = 'JSON') AS
SELECT
    category,
    COUNT(*) AS total
FROM
    labels
GROUP BY
    category;

CREATE TABLE scene_index WITH (KEY_FORMAT = 'JSON') AS
SELECT
    scene,
    COUNT(*) AS total
FROM
    labels
GROUP BY
    scene;

CREATE TABLE timeofday_index WITH (KEY_FORMAT = 'JSON') AS
SELECT
    timeofday,
    COUNT(*) AS total
FROM
    labels
GROUP BY
    timeofday;

CREATE TABLE weather_index WITH (KEY_FORMAT = 'JSON') AS
SELECT
    weather,
    COUNT(*) AS total
FROM
    labels
GROUP BY
    weather;

CREATE TABLE LABELS_INFO AS
SELECT
    *
FROM
    LABELS L
    INNER JOIN INFO I ON L.IMAGE_ID = I.IMAGE_ID;

CREATE TABLE LABELS_INFO_QUERY WITH (KEY_FORMAT = 'JSON') AS
SELECT
    *
FROM
    LABELS_INFO;