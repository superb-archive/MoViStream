CREATE TABLE labels (
    id VARCHAR PRIMARY KEY,
    category VARCHAR,
    scene VARCHAR,
    timeofday VARCHAR,
    weather VARCHAR
  ) WITH (
    KAFKA_TOPIC = 'labels',
    VALUE_FORMAT = 'JSON'
  );


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
SELECT *
FROM
info;


CREATE TABLE category_index
    WITH (KEY_FORMAT='JSON') AS
    SELECT
        category,
        COUNT(*) AS total
    FROM labels
    GROUP BY category;


CREATE TABLE scene_index
    WITH (KEY_FORMAT='JSON') AS
    SELECT
        scene,
        COUNT(*) AS total
    FROM labels
    GROUP BY scene;


CREATE TABLE timeofday_index
    WITH (KEY_FORMAT='JSON') AS
    SELECT
        timeofday,
        COUNT(*) AS total
    FROM labels
    GROUP BY timeofday;


CREATE TABLE weather_index
    WITH (KEY_FORMAT='JSON') AS
    SELECT
        weather,
        COUNT(*) AS total
    FROM labels
    GROUP BY weather;
