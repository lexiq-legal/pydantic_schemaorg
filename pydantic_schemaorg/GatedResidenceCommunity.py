from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Residence import Residence


class GatedResidenceCommunity(Residence):
    """Residence type: Gated community.

    See: https://schema.org/GatedResidenceCommunity
    Model depth: 4
    """
    type_: str = Field("GatedResidenceCommunity", alias='@type')
    

