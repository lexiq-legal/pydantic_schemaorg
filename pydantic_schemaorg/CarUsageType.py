from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class CarUsageType(Enumeration):
    """A value indicating a special usage of a car, e.g. commercial rental, driving school,"
     "or as a taxi.

    See: https://schema.org/CarUsageType
    Model depth: 4
    """
    type_: str = Field("CarUsageType", alias='@type')
    

