from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class TrainStation(CivicStructure):
    """A train station.

    See: https://schema.org/TrainStation
    Model depth: 4
    """
    type_: str = Field("TrainStation", alias='@type')
    

