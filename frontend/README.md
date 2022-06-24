# Frontend Web App for Autonomous Vehicle Monitoring

## Streamlit

Streamlit is a data visualization tool for python users.
Our Streamlit app queries data from KSQL and visualizes the result using various widgets.

### KSQL APIs

Instead of directly streaming the data straight from Kafka, we took the full advantage of KSQL, transforming and aggregating the stream of real-time data into the exact format we desire. This is an example of how we configured KSQL tables to aggregate the sum of each label category.
```bash
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
```
Since each message represents a unique data as opposed to an update of an existing data, we first created a table that continously reflect our stream of data. Then, we solidated an aggregation query that sums the count of each category by generating a materialized view table.
```bash
CREATE TABLE category_index WITH (KEY_FORMAT = 'JSON') AS
SELECT
    category,
    COUNT(*) AS total
FROM
    labels
GROUP BY
    category;
```
Given the materialized view, we could easily perform a pull query of the aggregation by `SELECT * FROM category_index`. Conclusively, KSQL allowed us to pull data every frontend app update tick and render a near real-time visualization of streaming data aggregation.

## Data

We visualize the following data at a user-defined interval.

### GPS & IMU

An example of an autonomous vehicle data is GPS data.
We visualize vehicle locations and trajectories on OpenStreetMap using deckgl.

Inertial measurement unit is another metric commonly collected from smart vehicles.
As an example, the accelerometer data is visualized using streamlit line charts.

### Image Labels

An autonomous vehicle has many visual receptors such as cameras and lidar sensors.
Thus, computer vision techniques are used to understand (**infer** on) the scene.

Compiled from multiple vehicles, the inference results (labels) can useful for city monitoring.
It can also be used by ML engineers or data scientists for collecting data (ex, rare labels).
As such, we visualize the collective label distribution with various filters as pie charts.

### Instructions

Run below command to get started.

```bash
$ streamlit run streamlit.py
```

Set configurations in the sidebar.


Interact with the web app.

