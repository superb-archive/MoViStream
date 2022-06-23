# Frontend Web App for Autonomous Vehicle Monitoring

## Streamlit

Streamlit is a data visualization toolkit built for python users.
It queries data from KSQL and visualizes the result using various widgets.

## Data

We visualize the following data at a user-defined interval.

### GPS & IMU

One use case of autonomous vehicle data is live localization with gps data.
We visualize vehicle locations and trajectories on OpenStreetMap using deckgl.

Inertial measurement unit is another metric commonly collected from smart vehicles.
The accelerometer & gyroscope data is visualized using streamlit line charts.

### Image Labels

An autonomous vehicle has many visual receptors such as cameras and lidar sensors.
Often, computer vision techniques are used to understand (**infer** on) the scene.

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

