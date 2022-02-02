from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RadioStation(LocalBusiness):
    """A radio station.

    See: https://schema.org/RadioStation
    Model depth: 4
    """
    type_: str = Field("RadioStation", alias='@type')
    

