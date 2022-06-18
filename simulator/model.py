from typing import List, Optional

from pydantic import BaseModel


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
