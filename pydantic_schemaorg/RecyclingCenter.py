from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class RecyclingCenter(LocalBusiness):
    """A recycling center.

    See: https://schema.org/RecyclingCenter
    Model depth: 4
    """
    type_: str = Field("RecyclingCenter", alias='@type')
    

