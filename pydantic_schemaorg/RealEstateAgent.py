from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RealEstateAgent(LocalBusiness):
    """A real-estate agent.

    See: https://schema.org/RealEstateAgent
    Model depth: 4
    """
    type_: str = Field("RealEstateAgent", alias='@type')
    

