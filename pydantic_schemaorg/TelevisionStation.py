from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TelevisionStation(LocalBusiness):
    """A television station.

    See: https://schema.org/TelevisionStation
    Model depth: 4
    """
    type_: str = Field("TelevisionStation", alias='@type')
    

