from typing import List, Optional

from pydantic import BaseModel, Field


class ImageAttribute(BaseModel):
    """
    - weather: "rainy|snowy|clear|overcast|undefined|partly cloudy|foggy"
    - scene: "tunnel|residential|parking lot|undefined|city street|gas stations|highway|"
    - timeofday: "daytime|night|dawn/dusk|undefined"
    """

    scene: str
    timeofday: str
    weather: str


class LabelAttribute(BaseModel):
    """
    - occluded: boolean
    - truncated: boolean
    - trafficLightColor: "red|green|yellow|none"
    - areaType: "direct | alternative" (for driving area)
    - laneDirection: "parallel|vertical" (for lanes)
    - laneStyle: "solid | dashed" (for lanes)
    - laneTypes: (for lanes)
    """

    occluded: Optional[bool]
    truncated: Optional[bool]
    trafficLightColor: Optional[str]


class Label(BaseModel):
    attributes: LabelAttribute
    category: str
    id: int
    manualAttributes: bool
    manualShape: bool


class LabelFlattened(BaseModel):
    image_id: str
    category: str
    id: str
    scene: str
    timeofday: str
    weather: str


class Image(BaseModel):
    attributes: ImageAttribute
    labels: List[Label]
    name: str
    timestamp: int


class XYZT(BaseModel):
    x: float
    y: float
    z: float
    timestamp: int


class Location(BaseModel):
    timestamp: int
    longitude: float
    latitude: float
    course: float
    speed: float
    accuracy: float


class GPS(BaseModel):
    timestamp: int
    altitude: float
    longitude: float
    vertical_accuracy: float = Field(alias="vertical accuracy")
    horizontal_accuracy: float = Field(alias="horizontal accuracy")
    latitude: float
    speed: float


class LocationFlattened(BaseModel):
    id: str
    image_id: str
    timestamp: int
    longitude: float
    latitude: float
    course: float
    speed: float
    accuracy: float


class Info(BaseModel):
    rideID: str
    accelerometer: List[XYZT]
    gyro: List[XYZT]
    timelapse: int
    locations: List[Location]
    filename: str
    startTime: int
    endTime: int
    gps: List[GPS]
