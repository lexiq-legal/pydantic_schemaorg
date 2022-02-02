from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EntertainmentBusiness(LocalBusiness):
    """A business providing entertainment.

    See: https://schema.org/EntertainmentBusiness
    Model depth: 4
    """
    type_: str = Field("EntertainmentBusiness", alias='@type')
    

