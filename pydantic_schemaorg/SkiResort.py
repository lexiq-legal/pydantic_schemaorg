from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Resort import Resort
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SkiResort(Resort, SportsActivityLocation):
    """A ski resort.

    See: https://schema.org/SkiResort
    Model depth: 5
    """
    type_: str = Field("SkiResort", alias='@type')
    

