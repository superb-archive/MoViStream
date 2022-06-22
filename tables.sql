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

CREATE TABLE locations (
    id VARCHAR PRIMARY KEY,
    image_id VARCHAR,
    "timestamp" INT,
    longitude DOUBLE,
    latitude DOUBLE,
    speed DOUBLE
) WITH (
    KAFKA_TOPIC = 'locations',
    VALUE_FORMAT = 'JSON'
);

CREATE TABLE locations_query WITH (KEY_FORMAT = 'JSON') AS
SELECT
    *
FROM
    locations;

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

-- CREATE TABLE LABELS_WITH_Locations AS

-- SELECT

--     *

-- FROM

--     LABELS L

--     INNER JOIN Locations G ON L.IMAGE_ID = G.IMAGE_ID;

-- CREATE TABLE LABELS_WITH_Locations_QUERY WITH (KEY_FORMAT = 'JSON') AS

-- SELECT

--     *

-- FROM

--     LABELS_WITH_Locations;