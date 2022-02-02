from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class VirtualLocation(Intangible):
    """An online or virtual location for attending events. For example, one may attend an online"
     "seminar or educational event. While a virtual location may be used as the location of"
     "an event, virtual locations should not be confused with physical locations in the real"
     "world.

    See: https://schema.org/VirtualLocation
    Model depth: 3
    """
    type_: str = Field("VirtualLocation", alias='@type')
    

