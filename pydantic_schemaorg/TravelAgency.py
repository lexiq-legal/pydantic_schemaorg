from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TravelAgency(LocalBusiness):
    """A travel agency.

    See: https://schema.org/TravelAgency
    Model depth: 4
    """
    type_: str = Field("TravelAgency", alias='@type')
    

